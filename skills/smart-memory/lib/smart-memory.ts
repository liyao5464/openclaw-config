import Database from 'better-sqlite3';
import { join } from 'path';
import { createHash } from 'crypto';

export interface SearchResult {
  id: string;
  path: string;
  content: string;
  title: string;
  score: number;
  rank: number;
}

export interface Chunk {
  hash: string;
  seq: number;
  pos: number;
  text: string;
}

export class SmartMemory {
  private db: Database.Database;
  private dbPath: string;

  constructor(dbPath: string = './memory.db') {
    this.dbPath = dbPath;
    this.db = new Database(dbPath);
  }

  async initialize(): Promise<void> {
    // Create tables
    this.db.exec(`
      CREATE TABLE IF NOT EXISTS documents (
        id TEXT PRIMARY KEY,
        path TEXT NOT NULL UNIQUE,
        content TEXT NOT NULL,
        title TEXT,
        created_at INTEGER DEFAULT (strftime('%s', 'now')),
        updated_at INTEGER DEFAULT (strftime('%s', 'now'))
      );

      CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts USING fts5(
        content, title,
        content='documents',
        content_rowid='rowid'
      );

      CREATE TABLE IF NOT EXISTS chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doc_id TEXT NOT NULL,
        hash TEXT NOT NULL,
        seq INTEGER NOT NULL,
        pos INTEGER NOT NULL,
        text TEXT NOT NULL,
        FOREIGN KEY (doc_id) REFERENCES documents(id)
      );

      CREATE INDEX IF NOT EXISTS idx_chunks_doc ON chunks(doc_id);
      
      CREATE TABLE IF NOT EXISTS contexts (
        path TEXT PRIMARY KEY,
        description TEXT
      );
    `);

    // Setup FTS triggers
    this.db.exec(`
      CREATE TRIGGER IF NOT EXISTS documents_ai AFTER INSERT ON documents BEGIN
        INSERT INTO documents_fts(rowid, content, title)
        VALUES (new.rowid, new.content, new.title);
      END;

      CREATE TRIGGER IF NOT EXISTS documents_au AFTER UPDATE ON documents BEGIN
        INSERT INTO documents_fts(documents_fts, rowid, content, title)
        VALUES ('delete', old.rowid, old.content, old.title);
        INSERT INTO documents_fts(rowid, content, title)
        VALUES (new.rowid, new.content, new.title);
      END;

      CREATE TRIGGER IF NOT EXISTS documents_ad AFTER DELETE ON documents BEGIN
        INSERT INTO documents_fts(documents_fts, rowid, content, title)
        VALUES ('delete', old.rowid, old.content, old.title);
      END;
    `);
  }

  /**
   * Generate short hash for document ID
   */
  private generateId(content: string): string {
    return createHash('sha256').update(content).digest('hex').substring(0, 8);
  }

  /**
   * Extract title from markdown content
   */
  private extractTitle(content: string): string {
    const match = content.match(/^#\s+(.+)$/m);
    return match ? match[1].trim() : '';
  }

  /**
   * Smart chunking with markdown-aware boundaries
   */
  smartChunk(content: string, targetTokens: number = 900, overlap: number = 0.15): Chunk[] {
    const breakScores: Record<string, number> = {
      '# ': 100,
      '## ': 90,
      '### ': 80,
      '#### ': 70,
      '##### ': 60,
      '###### ': 50,
      '```': 80,
      '---': 60,
      '***': 60,
      '\n\n': 20,
      '- ': 5,
      '1. ': 5,
    };

    const chunks: Chunk[] = [];
    const windowSize = Math.floor(targetTokens * overlap);
    let position = 0;
    let seq = 0;

    while (position < content.length) {
      const targetEnd = position + targetTokens;
      if (targetEnd >= content.length) {
        // Last chunk
        const text = content.slice(position);
        chunks.push({
          hash: this.generateId(text),
          seq: seq++,
          pos: position,
          text,
        });
        break;
      }

      // Find best break point within window
      const windowStart = Math.max(position, targetEnd - windowSize);
      let bestScore = 0;
      let bestPos = targetEnd;

      for (let i = windowStart; i < Math.min(targetEnd, content.length); i++) {
        const remaining = targetEnd - i;
        const distanceRatio = remaining / windowSize;
        
        for (const [pattern, baseScore] of Object.entries(breakScores)) {
          if (content.slice(i, i + pattern.length) === pattern) {
            const score = baseScore * (1 - distanceRatio * distanceRatio * 0.7);
            if (score > bestScore) {
              bestScore = score;
              bestPos = i;
            }
          }
        }
      }

      const text = content.slice(position, bestPos).trim();
      if (text) {
        chunks.push({
          hash: this.generateId(text),
          seq: seq++,
          pos: position,
          text,
        });
      }

      // Move position with overlap
      position = bestPos - Math.floor((bestPos - position) * overlap);
    }

    return chunks;
  }

  /**
   * Index a document
   */
  async indexDocument(path: string, content: string): Promise<void> {
    const id = this.generateId(path + content);
    const title = this.extractTitle(content);

    const insertDoc = this.db.prepare(`
      INSERT OR REPLACE INTO documents (id, path, content, title)
      VALUES (?, ?, ?, ?)
    `);

    insertDoc.run(id, path, content, title);

    // Delete old chunks
    const deleteChunks = this.db.prepare('DELETE FROM chunks WHERE doc_id = ?');
    deleteChunks.run(id);

    // Insert new chunks
    const chunks = this.smartChunk(content);
    const insertChunk = this.db.prepare(`
      INSERT INTO chunks (doc_id, hash, seq, pos, text)
      VALUES (?, ?, ?, ?, ?)
    `);

    for (const chunk of chunks) {
      insertChunk.run(id, chunk.hash, chunk.seq, chunk.pos, chunk.text);
    }
  }

  /**
   * BM25 full-text search
   */
  bm25Search(query: string, limit: number = 10): Array<{ id: string; score: number; doc: any }> {
    const stmt = this.db.prepare(`
      SELECT d.id, d.path, d.content, d.title,
             bm25(documents_fts) as score
      FROM documents_fts
      JOIN documents d ON documents_fts.rowid = d.rowid
      WHERE documents_fts MATCH ?
      ORDER BY bm25(documents_fts)
      LIMIT ?
    `);

    const results = stmt.all(query, limit);
    return results.map((r: any) => ({
      id: r.id,
      score: Math.abs(r.score),
      doc: r,
    }));
  }

  /**
   * RRF Fusion
   */
  rrfFusion(
    resultsLists: Array<Array<{ id: string; score: number }>>,
    k: number = 60,
    originalBoost: number = 2.0
  ): Map<string, number> {
    const scores = new Map<string, number>();

    for (let listIdx = 0; listIdx < resultsLists.length; listIdx++) {
      const weight = listIdx === 0 ? originalBoost : 1.0;
      const results = resultsLists[listIdx];

      for (let rank = 0; rank < results.length; rank++) {
        const id = results[rank].id;
        const rrfScore = weight / (k + rank + 1);
        
        let currentScore = scores.get(id) || 0;
        currentScore += rrfScore;

        // Top-rank bonus
        if (rank === 0) currentScore += 0.05;
        else if (rank <= 2) currentScore += 0.02;

        scores.set(id, currentScore);
      }
    }

    return scores;
  }

  /**
   * Hybrid search
   */
  async search(query: string, options: { limit?: number; minScore?: number } = {}): Promise<SearchResult[]> {
    const { limit = 5, minScore = 0.1 } = options;

    // BM25 search
    const bm25Results = this.bm25Search(query, limit * 2);

    // TODO: Add vector search when embeddings are available
    // For now, just use BM25
    const results: SearchResult[] = bm25Results.slice(0, limit).map((r, idx) => ({
      id: r.id,
      path: r.doc.path,
      content: r.doc.content.slice(0, 500), // Truncate for display
      title: r.doc.title,
      score: 1 / (1 + r.score), // Normalize
      rank: idx + 1,
    }));

    return results.filter(r => r.score >= minScore);
  }

  /**
   * Get document by ID
   */
  getDocument(id: string): { id: string; path: string; content: string; title: string } | null {
    const stmt = this.db.prepare('SELECT * FROM documents WHERE id = ?');
    const doc = stmt.get(id) as any;
    return doc ? {
      id: doc.id,
      path: doc.path,
      content: doc.content,
      title: doc.title,
    } : null;
  }

  /**
   * Get all indexed paths
   */
  getIndexedPaths(): string[] {
    const stmt = this.db.prepare('SELECT path FROM documents ORDER BY updated_at DESC');
    const results = stmt.all() as any[];
    return results.map(r => r.path);
  }

  close(): void {
    this.db.close();
  }
}

export default SmartMemory;
