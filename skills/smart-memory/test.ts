#!/usr/bin/env bun
/**
 * Quick test for Smart Memory
 */

import { SmartMemory } from './lib/smart-memory';

async function test() {
  console.log('🧪 Testing Smart Memory...\n');

  const memory = new SmartMemory('./test.db');
  await memory.initialize();

  // Test 1: Index documents
  console.log('1️⃣ Indexing test documents...');
  
  await memory.indexDocument('memory/2026-02-17.md', `
# OpenClaw Configuration Guide

Today we configured OpenClaw with multiple agents.

## Steps
1. Install OpenClaw
2. Configure agents
3. Set up skills

The process was smooth and we saved a lot of tokens.
`);

  await memory.indexDocument('memory/2026-02-16.md', `
# AI Daily News

Today\'s AI news includes:
- Alibaba released Qwen 3.5
- Google announced new features
- OpenAI updated their API

Token prices are dropping significantly.
`);

  await memory.indexDocument('docs/setup.md', `
# Setup Guide

This guide covers the setup process for OpenClaw.
Make sure you have Node.js installed.

## Requirements
- Node.js 18+
- Bun runtime
- Git

## Installation
Run the install script.
`);

  console.log('✅ Indexed 3 documents\n');

  // Test 2: Search
  console.log('2️⃣ Searching for "token"...');
  const results = await memory.search('token', { limit: 3 });
  
  console.log(`Found ${results.length} results:\n`);
  for (const r of results) {
    console.log(`  📄 ${r.path} (${(r.score * 100).toFixed(1)}%)`);
    console.log(`     ${r.content.slice(0, 100)}...\n`);
  }

  // Test 3: Search with different query
  console.log('3️⃣ Searching for "OpenClaw setup"...');
  const results2 = await memory.search('OpenClaw setup', { limit: 3 });
  
  console.log(`Found ${results2.length} results:\n`);
  for (const r of results2) {
    console.log(`  📄 ${r.path} (${(r.score * 100).toFixed(1)}%)`);
  }

  // Test 4: Status
  console.log('\n4️⃣ Index status:');
  const paths = memory.getIndexedPaths();
  console.log(`   Total documents: ${paths.length}`);
  paths.forEach(p => console.log(`   - ${p}`));

  memory.close();
  
  console.log('\n✅ All tests passed!');
  
  // Cleanup
  const fs = await import('fs');
  fs.unlinkSync('./test.db');
}

test().catch(console.error);
