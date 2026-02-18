#!/usr/bin/env python3
# ai_team_bot.py - AI助手团队消息中转
import asyncio
import aiohttp
import json
import time
from datetime import datetime

# Bot配置
BOTS = {
    'ceo': {
        'token': '8502623699:AAHvcI6KzV9aIOrSvRk_jR9mIdw_U9ltbvU',
        'name': 'CEO',
        'personality': '专业、果断、结果导向'
    },
    'content': {
        'token': '8410310347:AAGdeSOEmHbxI6Riuk2eVllyYEY7aupYJwM',
        'name': '内容总监',
        'personality': '创意、敏锐、追求完美'
    },
    'ops': {
        'token': '7893941242:AAFRzUTiVt9MFBF2vOegR2ZAirXfuai6a94',
        'name': '运营总监',
        'personality': '数据驱动、精细、增长黑客'
    }
}

CHAT_ID = '8404273573'

class AITeamBot:
    def __init__(self):
        self.last_ids = {'ceo': 0, 'content': 0, 'ops': 0}
        self.session = None
    
    async def start(self):
        self.session = aiohttp.ClientSession()
        print(f"[{datetime.now()}] AI助手团队服务启动")
        
        while True:
            try:
                for role, bot in BOTS.items():
                    await self.check_messages(role, bot)
                await asyncio.sleep(10)  # 每10秒检查一次
            except Exception as e:
                print(f"[{datetime.now()}] 错误: {e}")
                await asyncio.sleep(5)
    
    async def check_messages(self, role, bot):
        url = f"https://api.telegram.org/bot{bot['token']}/getUpdates"
        params = {
            'offset': self.last_ids[role],
            'limit': 10
        }
        
        async with self.session.get(url, params=params) as resp:
            data = await resp.json()
            
            if data.get('ok') and data.get('result'):
                for update in data['result']:
                    update_id = update['update_id']
                    if update_id >= self.last_ids[role]:
                        message = update.get('message', {})
                        text = message.get('text', '')
                        
                        if text and text != '/start':
                            print(f"[{datetime.now()}] [{role}] 收到: {text}")
                            await self.reply(role, bot, text)
                            self.last_ids[role] = update_id + 1
    
    async def reply(self, role, bot, user_text):
        # 根据角色生成回复
        if role == 'ceo':
            reply_text = f"老板好！📊\\n\\n收到您的指示：{user_text}\\n\\n作为CEO，我建议：\\n• 立即安排相关部门执行\\n• 今日内给您进度汇报\\n• 如有需要协调的，我来统筹"
        elif role == 'content':
            reply_text = f"老板好！🎯\\n\\n关于【{user_text}】\\n\\n【内容部建议】\\n• 本周可安排2-3个相关选题\\n• 预计产出1篇深度文章+2条短视频\\n• 需要老板确认具体内容方向"
        elif role == 'ops':
            reply_text = f"老板好！📈\\n\\n收到数据需求：{user_text}\\n\\n【运营部数据】\\n• 今日新增粉丝：___\\n• 昨日阅读量：___\\n• 本周累计：___\\n\\n详细报表正在整理，10分钟后发给您！"
        else:
            reply_text = f"收到：{user_text}"
        
        url = f"https://api.telegram.org/bot{bot['token']}/sendMessage"
        params = {
            'chat_id': CHAT_ID,
            'text': reply_text,
            'parse_mode': 'HTML'
        }
        
        async with self.session.get(url, params=params) as resp:
            result = await resp.json()
            if result.get('ok'):
                print(f"[{datetime.now()}] [{role}] 已回复")
    
    async def stop(self):
        if self.session:
            await self.session.close()

if __name__ == '__main__':
    bot = AITeamBot()
    try:
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        print(f"\\n[{datetime.now()}] 服务停止")
