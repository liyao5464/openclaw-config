#!/usr/bin/env bun
/**
 * Smart Memory MCP Server for OpenClaw
 * Replaces memory_search with hybrid BM25 + Vector retrieval
 */

import { SmartMemory } from '../lib/smart-memory';
import { resolve } from 'path';

const MEMORY_DIR = process.env.MEMORY_DIR || './memory';
const DB_PATH = process.env.SMART_MEMORY_DB || './.smart-memory.db';

interface MCPRequest {
  jsonrpc: '2.0';
  id: number | string;
  method: string;
  params?: any;
}

interface MCPResponse {
  jsonrpc: '2.0';
  id: number | string;
  result?: any;
  error?: { code: number; message: string };
}

class SmartMemoryMCPServer {
  private memory: SmartMemory;
  private initialized: boolean = false;

  constructor() {
    this.memory = new SmartMemory(DB_PATH);
  }

  async initialize(): Promise<void> {
    if (this.initialized) return;
    await this.memory.initialize();
    this.initialized = true;
    
    // Index existing memory files
    await this.indexMemoryFiles();
  }

  private async indexMemoryFiles(): Promise<void> {
    const fs = await import('fs');
    const path = await import('path');
    const { glob } = await import('glob');

    const files = await glob(`${MEMORY_DIR}/**/*.md`);
    
    for (const file of files) {
      const content = fs.readFileSync(file, 'utf-8');
      const relativePath = path.relative(process.cwd(), file);
      
      try {
        await this.memory.indexDocument(relativePath, content);
      } catch (e) {
        // Ignore duplicate errors
      }
    }
  }

  handleRequest(request: MCPRequest): MCPResponse {
    const { id, method, params } = request;

    try {
      switch (method) {
        case 'search':
          return { jsonrpc: '2.0', id, result: this.handleSearch(params) };
        case 'index':
          return { jsonrpc: '2.0', id, result: this.handleIndex(params) };
        case 'get':
          return { jsonrpc: '2.0', id, result: this.handleGet(params) };
        case 'status':
          return { jsonrpc: '2.0', id, result: this.handleStatus() };
        default:
          return {
            jsonrpc: '2.0',
            id,
            error: { code: -32601, message: `Method not found: ${method}` }
          };
      }
    } catch (error) {
      return {
        jsonrpc: '2.0',
        id,
        error: { code: -32603, message: String(error) }
      };
    }
  }

  private async handleSearch(params: any) {
    const { query, limit = 5, minScore = 0.1 } = params;
    
    const results = await this.memory.search(query, { limit, minScore });
    
    return {
      results: results.map(r => ({
        path: r.path,
        content: r.content,
        score: r.score,
        rank: r.rank,
      })),
      total: results.length,
    };
  }

  private async handleIndex(params: any) {
    const { path, content } = params;
    await this.memory.indexDocument(path, content);
    return { success: true, path };
  }

  private handleGet(params: any) {
    const { id } = params;
    const doc = this.memory.getDocument(id);
    return { document: doc };
  }

  private handleStatus() {
    const paths = this.memory.getIndexedPaths();
    return {
      dbPath: DB_PATH,
      indexedCount: paths.length,
      memoryDir: MEMORY_DIR,
    };
  }

  close(): void {
    this.memory.close();
  }
}

// Stdio MCP server
async function main() {
  const server = new SmartMemoryMCPServer();
  await server.initialize();

  process.stdin.setEncoding('utf-8');

  let buffer = '';
  
  process.stdin.on('data', (chunk) => {
    buffer += chunk;
    
    // Parse JSON-RPC messages (newline-delimited)
    const lines = buffer.split('\n');
    buffer = lines.pop() || ''; // Keep incomplete line

    for (const line of lines) {
      if (!line.trim()) continue;
      
      try {
        const request = JSON.parse(line) as MCPRequest;
        const response = server.handleRequest(request);
        process.stdout.write(JSON.stringify(response) + '\n');
      } catch (e) {
        console.error('Parse error:', e);
      }
    }
  });

  process.stdin.on('end', () => {
    server.close();
  });
}

main().catch(console.error);
