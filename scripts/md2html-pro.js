#!/usr/bin/env node
// md2html-pro.js - 微信兼容排版（全内联样式）
// 用法: node md2html-pro.js input.md [grace|wechat|tech|minimal]

const fs = require('fs');
const path = require('path');
const MARKED_PATH = path.join(__dirname, '../skills/baoyu-skills/skills/baoyu-markdown-to-html/node_modules/marked/lib/marked.cjs');
const { marked, Renderer } = require(MARKED_PATH);

const input = process.argv[2];
const theme = process.argv[3] || 'wechat';
if (!input) { console.error('用法: node md2html-pro.js input.md [grace|wechat|tech|minimal]'); process.exit(1); }

// ── 主题配置 ──────────────────────────────────────────
const THEMES = {
  wechat: {
    body:        'font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:17px;line-height:2;color:#333;max-width:680px;margin:0 auto;padding:32px 20px;background:#fff',
    h2:          'font-size:1.25em;font-weight:700;color:#2c2c2c;margin:2em 0 .6em;padding-bottom:8px;border-bottom:3px solid #9b4f2e;display:block',
    h3:          'font-size:1.1em;font-weight:700;color:#9b4f2e;margin:1.8em 0 .6em',
    p:           'margin:1.1em 0;color:#333;font-size:17px;line-height:2',
    strong:      'color:#9b4f2e;font-weight:700',
    em:          'color:#9b4f2e;font-style:normal',
    blockquote:  'margin:1.5em 0;padding:14px 20px;background:#fdf6f2;border-left:4px solid #9b4f2e;border-radius:0 8px 8px 0;color:#555',
    code_inline: 'background:#fdf0eb;padding:2px 7px;border-radius:4px;font-size:.88em;color:#9b4f2e;font-family:monospace',
    pre:         'background:#1e1e1e;color:#d4d4d4;padding:20px;border-radius:10px;overflow-x:auto;margin:1.5em 0',
    pre_code:    'background:none;color:#d4d4d4;padding:0;font-size:.9em;font-family:monospace',
    ul:          'padding-left:1.6em;margin:.8em 0',
    ol:          'padding-left:1.6em;margin:.8em 0',
    li:          'margin:.6em 0;color:#333',
    hr:          'border:none;height:1px;background:linear-gradient(90deg,transparent,#ddd,transparent);margin:2.5em 0',
    table:       'width:100%;border-collapse:collapse;margin:1.5em 0',
    th:          'background:#9b4f2e;color:#fff;padding:12px 16px;text-align:left;font-size:.95em',
    td:          'padding:11px 16px;border-bottom:1px solid #f0e8e4;color:#333',
    a:           'color:#9b4f2e;text-decoration:none',
  },
  grace: {
    body:        'font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:17px;line-height:2;color:#3a3a3a;max-width:680px;margin:0 auto;padding:32px 20px;background:#faf8f5',
    h2:          'font-size:1.2em;font-weight:700;color:#fff;background:linear-gradient(135deg,#b5845a,#8c5e38);padding:10px 20px;border-radius:10px;margin:2.2em 0 1em;display:block',
    h3:          'font-size:1.05em;font-weight:700;color:#8c5e38;border-left:4px solid #b5845a;padding-left:12px;margin:1.8em 0 .7em',
    p:           'margin:1em 0;color:#3a3a3a;font-size:17px;line-height:2',
    strong:      'color:#8c5e38;font-weight:700',
    em:          'color:#666;font-style:normal',
    blockquote:  'margin:1.5em 0;padding:16px 20px 16px 24px;background:#fff8f2;border-left:4px solid #b5845a;border-radius:0 10px 10px 0;color:#555',
    code_inline: 'background:#f0ebe4;padding:2px 7px;border-radius:4px;font-size:.88em;color:#8c5e38;font-family:monospace',
    pre:         'background:#2b2420;color:#f0e6d8;padding:20px;border-radius:12px;overflow-x:auto;margin:1.5em 0',
    pre_code:    'background:none;color:#f0e6d8;padding:0;font-size:.9em;font-family:monospace',
    ul:          'padding-left:1.6em;margin:.8em 0',
    ol:          'padding-left:1.6em;margin:.8em 0',
    li:          'margin:.5em 0;color:#3a3a3a',
    hr:          'border:none;height:2px;background:linear-gradient(90deg,transparent,#d4b896,transparent);margin:2.5em 0',
    table:       'width:100%;border-collapse:collapse;margin:1.5em 0',
    th:          'background:#b5845a;color:#fff;padding:12px 16px;text-align:left;font-size:.95em',
    td:          'padding:11px 16px;border-bottom:1px solid #ede5d8;color:#3a3a3a',
    a:           'color:#b5845a;text-decoration:none',
  },
};

// ── 自定义渲染器（全内联样式，marked v4 API）─────────
function buildRenderer(t) {
  const renderer = new Renderer();

  // marked v4: 参数为普通字符串
  renderer.heading = function(text, depth) {
    if (depth === 2) return `<h2 style="${t.h2}">${text}</h2>\n`;
    if (depth === 3) return `<h3 style="${t.h3}">${text}</h3>\n`;
    return `<h${depth}>${text}</h${depth}>\n`;
  };

  renderer.paragraph = function(text) {
    return `<p style="${t.p}">${text}</p>\n`;
  };

  renderer.strong = function(text) {
    return `<strong style="${t.strong}">${text}</strong>`;
  };

  renderer.em = function(text) {
    return `<em style="${t.em}">${text}</em>`;
  };

  renderer.blockquote = function(quote) {
    return `<blockquote style="${t.blockquote}">${quote}</blockquote>\n`;
  };

  renderer.codespan = function(code) {
    return `<code style="${t.code_inline}">${code}</code>`;
  };

  renderer.code = function(code, lang) {
    return `<pre style="${t.pre}"><code style="${t.pre_code}">${code}</code></pre>\n`;
  };

  renderer.list = function(body, ordered) {
    const tag = ordered ? 'ol' : 'ul';
    const s = ordered ? t.ol : t.ul;
    return `<${tag} style="${s}">${body}</${tag}>\n`;
  };

  renderer.listitem = function(text) {
    return `<li style="${t.li}">${text}</li>\n`;
  };

  renderer.hr = function() {
    return `<hr style="${t.hr}">\n`;
  };

  renderer.link = function(href, title, text) {
    return `<a href="${href}" style="${t.a}">${text}</a>`;
  };

  renderer.table = function(header, body) {
    return `<table style="${t.table}"><thead>${header}</thead><tbody>${body}</tbody></table>\n`;
  };

  renderer.tablerow = function(content) {
    return `<tr>${content}</tr>\n`;
  };

  renderer.tablecell = function(content, flags) {
    if (flags && flags.header) return `<th style="${t.th}">${content}</th>`;
    return `<td style="${t.td}">${content}</td>`;
  };

  return renderer;
}


// ── 主流程 ────────────────────────────────────────────
const t = THEMES[theme] || THEMES.wechat;
const renderer = buildRenderer(t);

const md = fs.readFileSync(input, 'utf8');
const content = md.replace(/^---[\s\S]*?---\n/, '').replace(/^# .+\n/, '');
const body = marked.parse(content, { renderer });

const html = `<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
</head>
<body>
<div style="${t.body}">
${body}
</div>
</body>
</html>`;

const suffix = theme === 'grace' ? '' : `-${theme}`;
const out = input.replace(/\.md$/, `${suffix}.html`);
fs.writeFileSync(out, html);
console.log(out);
