#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")
VALID_STATES = ["idle", "writing", "researching", "executing", "syncing", "error"]

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"state": "idle", "detail": "等待任务中...", "progress": 0, "updated_at": datetime.now().isoformat()}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python set_state.py <state> [detail]")
        print(f"有效状态: {', '.join(VALID_STATES)}")
        sys.exit(1)
    
    s = sys.argv[1]
    if s not in VALID_STATES:
        print(f"错误: 无效状态 '{s}'")
        print(f"有效状态: {', '.join(VALID_STATES)}")
        sys.exit(1)
    
    state = load_state()
    state["state"] = s
    state["detail"] = sys.argv[2] if len(sys.argv) > 2 else ""
    state["updated_at"] = datetime.now().isoformat()
    save_state(state)
    print(f"状态已更新: {s} - {state['detail']}")
