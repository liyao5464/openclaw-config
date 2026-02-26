#!/bin/bash
# 批量导入 OpenClaw 文档到 NotebookLM

cd /root/.openclaw/workspace

# 设置 notebook
export NOTEBOOKLM_STORAGE=/root/.notebooklm/storage_state.json

# 获取 URL 列表
URLS=$(curl -s "https://docs.openclaw.ai/sitemap.xml" | grep -o '<loc>[^<]*</loc>' | sed 's/<loc>//g;s/<\/loc>//g')

# 切换到 notebook
notebooklm use 6125bc95

count=0
for url in $URLS; do
  count=$((count + 1))
  echo "[$count] Adding: $url"
  notebooklm source add "$url" 2>&1
  sleep 1  # 避免太快被限流
done

echo "Done! Total: $count"
