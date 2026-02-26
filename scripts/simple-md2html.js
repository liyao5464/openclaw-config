#!/usr/bin/env node
// simple-md2html.js - 简单 Markdown 转微信兼容 HTML（Grace 主题）
const fs = require('fs');
const path = require('path');

const MARKED_PATH = path.join(__dirname, '../skills/baoyu-skills/skills/baoyu-markdown-to-html/node_modules/marked/lib/marked.cjs');
const { marked } = require(MARKED_PATH);

const input = process.argv[2];
if (!input) { console.error('用法: node simple-md2html.js input.md'); process.exit(1); }

const md = fs.readFileSync(input, 'utf8');

// 去掉 frontmatter 和第一个 h1 标题
const content = md
  .replace(/^---[\s\S]*?---\n/, '')
  .replace(/^# .+\n/, '');

const body = marked.parse(content);

const html = `<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  body{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Source Han Sans CN",sans-serif;font-size:17px;line-height:2;color:#333;max-width:680px;margin:0 auto;padding:24px 20px;background:#faf8f5}
  h2{font-size:1.25em;font-weight:700;color:#fff;background:linear-gradient(135deg,#b5845a,#8c5e38);padding:10px 18px;border-radius:8px;margin:2em 0 1em;letter-spacing:0.05em}
  h3{font-size:1.05em;font-weight:700;color:#8c5e38;border-left:4px solid #b5845a;padding-left:12px;margin:1.5em 0 0.6em}
  p{margin:0.9em 0;color:#3a3a3a}
  strong{color:#8c5e38;font-weight:700}
  em{color:#666;font-style:normal;font-size:0.95em}
  blockquote{border-left:none;margin:1.2em 0;padding:14px 18px;background:#fff;border-radius:10px;box-shadow:0 2px 12px rgba(181,132,90,0.12);color:#555;position:relative}
  blockquote::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:linear-gradient(180deg,#b5845a,#d4a574);border-radius:4px 0 0 4px}
  code{background:#f0ebe4;padding:2px 7px;border-radius:4px;font-size:0.88em;color:#8c5e38;font-family:monospace}
  pre{background:#2b2420;color:#f0e6d8;padding:18px;border-radius:10px;overflow-x:auto;margin:1.2em 0}
  pre code{background:none;color:inherit;padding:0;font-size:0.9em}
  ul,ol{padding-left:1.6em;margin:0.8em 0}
  li{margin:0.5em 0;color:#3a3a3a}
  li::marker{color:#b5845a}
  hr{border:none;height:1px;background:linear-gradient(90deg,transparent,#d4b896,transparent);margin:2.5em 0}
  table{width:100%;border-collapse:collapse;margin:1.2em 0;border-radius:8px;overflow:hidden}
  th{background:#b5845a;color:#fff;padding:10px 14px;text-align:left;font-weight:600;font-size:0.95em}
  td{padding:10px 14px;border-bottom:1px solid #ede5d8;color:#3a3a3a}
  tr:nth-child(even) td{background:#fdf9f5}
  a{color:#b5845a;text-decoration:none}
  section.footnotes{margin-top:3em;padding-top:1.5em;border-top:1px solid #e8ddd0;font-size:0.9em;color:#888}
</style>
</head>
<body>
${body}
</body>
</html>`;

const out = input.replace(/\.md$/, '.html');
fs.writeFileSync(out, html);
console.log(out);
