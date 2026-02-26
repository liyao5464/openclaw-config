# OpenClaw Multi-Agent Setup with Multiple AI Assistants

Source: LumaDock Tutorial
URL: https://lumadock.com/tutorials/openclaw-multi-agent-setup

## Summary

OpenClaw supports running multiple agents inside one Gateway process, and each one can behave like its own assistant with its own files, memory, auth and tools.

## Key Patterns

### Persistent Agents
Persistent agents are long-lived ones that you define in config or create using the agent wizard. These are bound to channels and chats.

Examples:
- Work assistant bound to Slack
- Family assistant bound to WhatsApp with strict tool restrictions
- Coding assistant bound to Discord that can access repos and run commands
- Social agent that only writes drafts and never has exec enabled

### Sub-Agents
Sub-agents are background workers spawned from a running conversation. They run in their own session, do their job and post back a result.

Sub-agents are great for:
- Parallel research
- Slow tool tasks
- Cost control (use cheaper models for sub-agents)

## When Multi-Agent Makes Sense

1. **Different tool policies for safety** - Personal assistant needs exec/filesystem, but public Discord bot should not have exec
2. **Separate memories and tone** - Prevents "bleed" between different contexts
3. **Different models and cost profiles** - Fast model for casual chat, slower stronger model for deep work

## Setup Commands

```bash
# Create agents using wizard
openclaw agents add work
openclaw agents add coding
openclaw agents add alerts

# List bindings
openclaw agents list --bindings
```

## Key Concepts

- Each agent can have its own workspace, memory, session history, auth profiles, skills, and model selection
- They share the same server process and main config file
- Bindings determine which agent handles incoming messages
- Common binding fields: channel, accountId, peer, guild
