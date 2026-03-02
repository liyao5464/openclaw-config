#!/usr/bin/env node
// raphael-render.js - 用 Raphael 主题渲染 Markdown 为微信公众号 HTML
// 用法: node raphael-render.js <md文件> [主题名] > output.html
// 主题: apple(默认) | claude | wechat | notion | stripe

const fs = require('fs');
const { execSync } = require('child_process');

// 确保 markdown-it 已安装
try { require.resolve('markdown-it'); } catch(e) {
  execSync('npm install -g markdown-it', { stdio: 'inherit' });
}
const MarkdownIt = require('markdown-it');

const THEMES = {
  apple: {
    container: 'max-width:100%;margin:0 auto;padding:24px 20px 48px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-size:16px;line-height:1.7!important;color:#1d1d1f!important;background-color:#ffffff!important;word-wrap:break-word;',
    h1:'font-size:32px;font-weight:700;color:#111!important;line-height:1.3!important;margin:38px 0 16px;letter-spacing:-0.015em;',
    h2:'font-size:26px;font-weight:600;color:#111!important;line-height:1.35!important;margin:32px 0 16px;',
    h3:'font-size:21px;font-weight:600;color:#1d1d1f!important;line-height:1.4!important;margin:28px 0 14px;',
    p:'margin:18px 0!important;line-height:1.7!important;color:#1d1d1f!important;',
    strong:'font-weight:700;color:#000!important;',
    em:'font-style:italic;color:#666!important;',
    a:'color:#0066cc!important;text-decoration:none;border-bottom:1px solid #0066cc;',
    ul:'margin:16px 0;padding-left:28px;',ol:'margin:16px 0;padding-left:28px;',
    li:'margin:8px 0;line-height:1.7!important;color:#1d1d1f!important;',
    blockquote:'margin:24px 0;padding:16px 20px;background-color:#f5f5f7!important;border-left:4px solid #0066cc;color:#555!important;border-radius:4px;',
    code:'font-family:"SF Mono",Consolas,monospace;padding:3px 6px;background-color:#f5f5f7!important;color:#0066cc!important;border-radius:4px;font-size:12px!important;',
    pre:'margin:24px 0;padding:20px;background-color:#f5f5f7!important;border-radius:8px;overflow-x:auto;font-size:12px!important;',
    hr:'margin:36px auto;border:none;height:1px;background-color:#eaeaea!important;width:100%;',
    img:'max-width:100%;height:auto;display:block;margin:24px auto;border-radius:12px;',
  },
  claude: {
    container:'max-width:100%;margin:0 auto;padding:24px 20px 48px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-size:16px;line-height:1.7!important;color:#2b2b2b!important;background-color:#f8f6f0!important;word-wrap:break-word;',
    h1:'font-size:32px;font-weight:700;color:#b75c3d!important;line-height:1.3!important;margin:38px 0 16px;',
    h2:'font-size:26px;font-weight:600;color:#b75c3d!important;line-height:1.35!important;margin:32px 0 16px;',
    h3:'font-size:21px;font-weight:600;color:#2b2b2b!important;line-height:1.4!important;margin:28px 0 14px;',
    p:'margin:18px 0!important;line-height:1.7!important;color:#2b2b2b!important;',
    strong:'font-weight:700;color:#b75c3d!important;background-color:rgba(183,92,61,0.08);padding:0 4px;border-radius:4px;',
    em:'font-style:italic;color:#666!important;',
    a:'color:#b75c3d!important;text-decoration:none;border-bottom:1px solid #b75c3d;',
    ul:'margin:16px 0;padding-left:28px;',ol:'margin:16px 0;padding-left:28px;',
    li:'margin:8px 0;line-height:1.7!important;color:#2b2b2b!important;',
    blockquote:'margin:24px 0;padding:16px 20px;background-color:rgba(183,92,61,0.04)!important;border-left:4px solid #b75c3d;color:#555!important;border-radius:4px;',
    code:'font-family:"SF Mono",Consolas,monospace;padding:3px 6px;background-color:#f0ece4!important;color:#b75c3d!important;border-radius:4px;font-size:12px!important;',
    pre:'margin:24px 0;padding:20px;background-color:#f0ece4!important;border-radius:8px;overflow-x:auto;font-size:12px!important;',
    hr:'margin:36px auto;border:none;height:1px;background-color:#eaeaea!important;width:100%;',
    img:'max-width:100%;height:auto;display:block;margin:24px auto;border-radius:4px;',
  },
  wechat: {
    container:'max-width:100%;margin:0 auto;padding:24px 20px 48px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-size:16px;line-height:1.7!important;color:#333!important;background-color:#fff!important;word-wrap:break-word;',
    h1:'font-size:32px;font-weight:700;color:#111!important;line-height:1.3!important;margin:38px 0 16px;',
    h2:'font-size:26px;font-weight:600;color:#111!important;line-height:1.35!important;margin:32px 0 16px;',
    h3:'font-size:21px;font-weight:600;color:#333!important;line-height:1.4!important;margin:28px 0 14px;',
    p:'margin:18px 0!important;line-height:1.7!important;color:#333!important;',
    strong:'font-weight:700;color:#07c160!important;background-color:rgba(7,193,96,0.08);padding:0 4px;border-radius:4px;',
    em:'font-style:italic;color:#666!important;',
    a:'color:#07c160!important;text-decoration:none;border-bottom:1px solid #07c160;',
    ul:'margin:16px 0;padding-left:28px;',ol:'margin:16px 0;padding-left:28px;',
    li:'margin:8px 0;line-height:1.7!important;color:#333!important;',
    blockquote:'margin:24px 0;padding:16px 20px;background-color:#f0f7f2!important;border-left:4px solid #07c160;color:#555!important;border-radius:4px;',
    code:'font-family:"SF Mono",Consolas,monospace;padding:3px 6px;background-color:#f0f7f2!important;color:#07c160!important;border-radius:4px;font-size:12px!important;',
    pre:'margin:24px 0;padding:20px;background-color:#f0f7f2!important;border-radius:8px;overflow-x:auto;font-size:12px!important;',
    hr:'margin:36px auto;border:none;height:1px;background-color:#eaeaea!important;width:100%;',
    img:'max-width:100%;height:auto;display:block;margin:24px auto;border-radius:8px;',
  }
};

const mdFile = process.argv[2];
const themeName = process.argv[3] || 'claude';

if (!mdFile) { console.error('用法: node raphael-render.js <md文件> [主题]'); process.exit(1); }

const theme = THEMES[themeName] || THEMES.apple;
const md = new MarkdownIt({ html: true, linkify: true });

let content = fs.readFileSync(mdFile, 'utf-8');
// 去掉 frontmatter
content = content.replace(/^---[\s\S]*?---\n/, '');

let html = md.render(content);

// 应用内联样式
const tagMap = { h1:'h1',h2:'h2',h3:'h3',p:'p',strong:'strong',em:'em',a:'a',ul:'ul',ol:'ol',li:'li',blockquote:'blockquote',code:'code',pre:'pre',hr:'hr',img:'img' };
for (const [tag, key] of Object.entries(tagMap)) {
  if (!theme[key]) continue;
  html = html.replace(new RegExp(`<${tag}([ >])`, 'g'), `<${tag} style="${theme[key]}"$1`);
}

console.log(`<div style="${theme.container}">${html}</div>`);
