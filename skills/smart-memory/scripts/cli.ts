#!/usr/bin/env bun
/**
 * Smart Memory CLI
 * Hybrid search for documents with BM25 + Vector fusion
 */

import { SmartMemory } from './lib/smart-memory';
import { existsSync } from 'fs';
import { resolve } from 'path';

const DB_PATH = process.env.SMART_MEMORY_DB || './memory.db';

async function main() {
  const args = process.argv.slice(2);
  const command = args[0];

  const memory = new SmartMemory(DB_PATH);
  await memory.initialize();

  try {
    switch (command) {
      case 'index':
        await indexCommand(memory, args.slice(1));
        break;
      case 'search':
        await searchCommand(memory, args.slice(1));
        break;
      case 'query':
        await queryCommand(memory, args.slice(1));
        break;
      case 'status':
        await statusCommand(memory);
        break;
      case 'get':
        await getCommand(memory, args.slice(1));
        break;
      default:
        showHelp();
    }
  } finally {
    memory.close();
  }
}

async function indexCommand(memory: SmartMemory, args: string[]) {
  if (args.length < 2) {
    console.log('Usage: smart-memory index <path> <content>');
    process.exit(1);
  }

  const [path, ...contentParts] = args;
  const content = contentParts.join(' ');

  console.log(`Indexing: ${path}`);
  await memory.indexDocument(path, content);
  console.log('✅ Indexed successfully');
}

async function searchCommand(memory: SmartMemory, args: string[]) {
  if (args.length < 1) {
    console.log('Usage: smart-memory search <query> [--limit N]');
    process.exit(1);
  }

  const query = args[0];
  const limitArg = args.find(arg => arg.startsWith('--limit='));
  const limit = limitArg ? parseInt(limitArg.split('=')[1]) : 5;

  console.log(`Searching: "${query}"\n`);
  
  const results = await memory.search(query, { limit });
  
  if (results.length === 0) {
    console.log('No results found');
    return;
  }

  for (const result of results) {
    console.log(`${result.path} #${result.id}`);
    console.log(`Title: ${result.title || '(no title)'}`);
    console.log(`Score: ${(result.score * 100).toFixed(1)}%`);
    console.log(`Content: ${result.content.slice(0, 200)}...`);
    console.log('---');
  }
}

async function queryCommand(memory: SmartMemory, args: string[]) {
  if (args.length < 1) {
    console.log('Usage: smart-memory query <query> [--all] [--files]');
    process.exit(1);
  }

  const query = args[0];
  const showAll = args.includes('--all');
  const filesOnly = args.includes('--files');

  console.log(`Query: "${query}"\n`);

  // Hybrid search (BM25 for now)
  const results = await memory.search(query, { 
    limit: showAll ? 50 : 5,
    minScore: 0.05
  });

  if (results.length === 0) {
    console.log('No results found');
    return;
  }

  if (filesOnly) {
    for (const result of results) {
      console.log(`${result.path},${result.score.toFixed(3)},#${result.id}`);
    }
  } else {
    for (const result of results) {
      console.log(`\n📄 ${result.path}`);
      console.log(`   ID: #${result.id}`);
      console.log(`   Score: ${(result.score * 100).toFixed(1)}%`);
      console.log(`   ${result.content.slice(0, 300)}...`);
    }
  }
}

async function statusCommand(memory: SmartMemory) {
  const paths = memory.getIndexedPaths();
  
  console.log('Smart Memory Status\n');
  console.log(`Database: ${DB_PATH}`);
  console.log(`Indexed documents: ${paths.length}`);
  
  if (paths.length > 0) {
    console.log('\nRecent documents:');
    paths.slice(0, 10).forEach(p => console.log(`  - ${p}`));
  }
}

async function getCommand(memory: SmartMemory, args: string[]) {
  if (args.length < 1) {
    console.log('Usage: smart-memory get <id-or-path>');
    process.exit(1);
  }

  const idOrPath = args[0];
  let doc;

  if (idOrPath.startsWith('#')) {
    // Get by ID
    doc = memory.getDocument(idOrPath.slice(1));
  } else {
    // Find by path (simplified - just show error)
    console.log('Use ID with # prefix, e.g., #abc123');
    return;
  }

  if (!doc) {
    console.log('Document not found');
    return;
  }

  console.log(`📄 ${doc.path}`);
  console.log(`ID: #${doc.id}`);
  console.log(`Title: ${doc.title || '(no title)'}`);
  console.log('\n---\n');
  console.log(doc.content);
}

function showHelp() {
  console.log(`
Smart Memory - Hybrid document search

Commands:
  index <path> <content>     Index a document
  search <query>             BM25 search
  query <query>             Hybrid search (BM25 + future vector)
  get <#id>                 Retrieve document by ID
  status                     Show index status

Options:
  --limit=N                  Number of results (default: 5)
  --all                      Return all matches
  --files                    Output as CSV (path,score,id)

Examples:
  smart-memory index "notes/2026-02-17.md" "# Meeting Notes\n..."
  smart-memory search "authentication flow" --limit=10
  smart-memory query "API design" --all --files
  smart-memory get #abc123
`);
}

main().catch(console.error);
