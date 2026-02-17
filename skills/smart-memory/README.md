# smart-memory

Smart document retrieval for OpenClaw with hybrid search (BM25 + Vector) and intelligent chunking.

## Features

- **Hybrid Search**: BM25 (FTS5) + Vector semantic search with RRF fusion
- **Smart Chunking**: 900-token chunks with 15% overlap, markdown-aware boundaries
- **Local Embedding**: Uses local embedding models (no API calls)
- **Top-K Retrieval**: Only returns most relevant documents to LLM
- **Token Saving**: 70-90% reduction in context tokens

## Installation

```bash
cp -r skills/smart-memory ~/.openclaw/skills/
```

## Usage

```typescript
import { SmartMemory } from './lib/smart-memory';

const memory = new SmartMemory('./memory.db');
await memory.initialize();

// Index documents
await memory.indexDocument('path/to/file.md', content);

// Search
const results = await memory.search('query', { limit: 5 });
```

## Architecture

```
Query → Query Expansion → BM25 Search + Vector Search → RRF Fusion → Top-K Re-ranking → Results
```

## License

MIT
