#!/usr/bin/env python3
"""
Workspace Incubation Scanner
每天凌晨自动扫描，追踪项目成熟度
"""

import os
import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path(os.environ.get('WORKSPACE', '/root/.openclaw/workspace'))
INCUBATOR_DIR = WORKSPACE / 'incubator'
INDEX_FILE = INCUBATOR_DIR / 'index.md'
LOG_FILE = INCUBATOR_DIR / 'logs' / f'{datetime.now().strftime("%Y-%m-%d")}.md'
CRON_RUNS_DIR = Path('/root/.openclaw/cron/runs')

TRACK_DIRS = ['skills', 'scripts', 'agents']
MATURITY_DAYS = 7
ERROR_PATTERNS = ['error', 'exception', 'traceback', 'failed', 'failure', '失败', '报错']


def scan_cron_errors_today() -> dict:
    """扫描今日 cron runs，返回出错的 job_id 列表"""
    if not CRON_RUNS_DIR.exists():
        return 

    today = datetime.now().date()
    errors = {}

    for f in CRON_RUNS_DIR.glob('*.jsonl'):
        try:
            for line in f.read_text().splitlines():
                if not line.strip():
                    continue
                record = json.loads(line)
                ts = record.get('ts', 0) / 1000
                if datetime.fromtimestamp(ts).date() != today:
                    continue
                if record.get('status') == 'error' or record.get('action') == 'error':
                    errors[record.get('jobId', f.stem)] = record.get('summary', record.get('error', ''))
        except Exception:
            continue

    return errors


def scan_log_errors_today(project_name: str) -> bool:
    """扫描 /tmp/*.log 里是否有今日与该项目相关的报错"""
    name_key = project_name.lower().replace('-', '').replace('_', '')

    for log_file in Path('/tmp').glob('*.log'):
        try:
            for line in log_file.read_text(errors='ignore').splitlines():
                ll = line.lower()
                if name_key in ll.replace('-', '').replace('_', ''):
                    if any(p in ll for p in ERROR_PATTERNS):
                        return True
        except Exception:
            continue

    return False


def scan_workspace() -> dict:
    """扫描workspace，返回所有可追踪项目"""
    projects = {}
    for dir_name in TRACK_DIRS:
        dir_path = WORKSPACE / dir_name
        if not dir_path.exists():
            continue
        for item in dir_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                has_skill = (item / 'SKILL.md').exists()
                has_script = any(item.glob('*.sh')) or any(item.glob('*.py'))
                if has_skill or has_script:
                    projects[item.name] = {
                        'path': f'{dir_name}/{item.name}',
                        'type': 'skill' if has_skill else 'script',
                    }
    return projects


def load_index() -> dict:
    """从 index.md 解析现有项目状态"""
    if not INDEX_FILE.exists():
        return {}
    projects = {}
    in_table = False
    for line in INDEX_FILE.read_text().splitlines():
        if line.startswith('| # |'):
            in_table = True
            continue
        if not in_table or not line.startswith('|'):
            continue
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 9 and parts[1].isdigit():
            projects[parts[2]] = {
                'path':         parts[3],
                'phase':        parts[4],
                'stable_days':  int(parts[5]) if parts[5].isdigit() else 0,
                'last_error':   parts[6],
                'harvest_type': parts[7],
            }
    return projects


def determine_phase(stable_days: int) -> str:
    if stable_days >= MATURITY_DAYS:
        return '🍎'
    elif stable_days >= MATURITY_DAYS - 2:
        return '🌳'
    elif stable_days >= 3:
        return '🌿'
    return '🌱'


def guess_harvest_type(name: str) -> str:
    n = name.lower()
    if any(k in n for k in ['skill', 'trainer', 'memory']):
        return '开源Skill'
    elif any(k in n for k in ['writing', 'post', 'article', 'blog']):
        return '教程'
    elif any(k in n for k in ['digest', 'news', 'daily']):
        return '推文'
    return '待定'


def save_index(projects: dict):
    phase_order = {'🍎': 0, '🌳': 1, '🌿': 2, '🌱': 3}
    sorted_p = sorted(projects.items(), key=lambda x: phase_order.get(x[1].get('phase', '🌱'), 4))

    lines = [
        "# Workspace 孵化系统", "",
        "每日自动扫描，追踪所有在孵项目的成熟度。", "",
        "## 阶段定义", "",
        "| 阶段 | 标记 | 含义 |",
        "|------|------|------|",
        "| 萌芽 | 🌱 | 刚创建，还不稳定 |",
        "| 生长 | 🌿 | 在使用中，偶尔有问题 |",
        "| 成熟 | 🌳 | 连续7天稳定，可以收割 |",
        "| 可收割 | 🍎 | 生成收割报告，待处理 |", "",
        "## 收割方向", "",
        "- `推文` → 适合发Twitter/X",
        "- `教程` → 适合写公众号文章",
        "- `开源Skill` → 适合做成可安装的Skill",
        "- `工具` → 适合做成独立工具", "",
        "## 追踪项目", "",
        "| # | 项目 | 路径 | 阶段 | 稳定天数 | 最后报错 | 收割方向 | 最后更新 |",
        "|---|------|------|------|---------|---------|---------|---------|",
    ]

    today = datetime.now().strftime('%Y-%m-%d')
    for idx, (name, info) in enumerate(sorted_p, 1):
        lines.append(
            f"| {idx} | {name} | {info.get('path','-')} | {info.get('phase','🌱')} "
            f"| {info.get('stable_days',0)} | {info.get('last_error','-')} "
            f"| {info.get('harvest_type','-')} | {today} |"
        )

    lines += ["", "---",
              f"*此文件由孵化系统自动更新，最后扫描: {datetime.now().strftime('%Y-%m-%d %H:%M')}*"]
    INDEX_FILE.write_text('\n'.join(lines))


def main():
    print(f"[孵化系统] 开始扫描 {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    INCUBATOR_DIR.mkdir(parents=True, exist_ok=True)
    (INCUBATOR_DIR / 'logs').mkdir(parents=True, exist_ok=True)

    # 今日 cron 报错
    cron_errors = scan_cron_errors_today()

    existing = load_index()
    current = scan_workspace()

    updated = {}
    new_mature = []

    for name, info in current.items():
        old = existing.get(name, {})
        old_days = old.get('stable_days', 0)

        # 检测今日是否有报错
        has_error = (
            scan_log_errors_today(name) or
            any(name.lower() in str(v).lower() for v in cron_errors.values())
        )

        if has_error:
            new_days = 0
            last_error = datetime.now().strftime('%Y-%m-%d')
        else:
            new_days = old_days + 1
            last_error = old.get('last_error', '-')

        new_phase = determine_phase(new_days)

        # 新成熟
        if old.get('phase') not in ('🍎',) and new_phase == '🍎':
            new_mature.append((name, {**old, 'harvest_type': old.get('harvest_type', guess_harvest_type(name))}))

        updated[name] = {
            'path':         info['path'],
            'phase':        new_phase,
            'stable_days':  new_days,
            'last_error':   last_error,
            'harvest_type': old.get('harvest_type', guess_harvest_type(name)),
        }

    save_index(updated)

    # 写日志
    harvest_lines = '\n'.join(f"- **{n}** → {i.get('harvest_type','待定')}" for n, i in new_mature) or '无'
    error_lines = '\n'.join(f"- {k}: {v[:80]}" for k, v in cron_errors.items()) or '无'

    LOG_FILE.write_text(f"""# 扫描日志 {datetime.now().strftime('%Y-%m-%d')}

## 扫描结果
- 追踪项目: {len(updated)} 个
- 今日报错: {len(cron_errors)} 个
- 新成熟: {len(new_mature)} 个

## 今日报错
{error_lines}

## 新成熟项目（可收割）
{harvest_lines}
""")

    print(f"[孵化系统] 完成！追踪: {len(updated)} 个，报错: {len(cron_errors)} 个，新成熟: {len(new_mature)} 个")

    if new_mature:
        names = '、'.join(n for n, _ in new_mature)
        os.system(f'openclaw system event --text "🍎 孵化系统：{names} 已成熟，可以收割了！" --mode now 2>/dev/null || true')


if __name__ == '__main__':
    main()
