# Feishu Operations Skill

This skill provides Feishu (Lark) group chat and messaging operations for OpenClaw agents.

## What This Skill Does

- Create and manage Feishu group chats
- Add members to group chats
- Send messages to groups or users
- Query group information and member lists

## When to Use This Skill

Use this skill when you need to:
- Create a new group chat for team discussions
- Add users to an existing group chat
- Send notifications or messages via Feishu
- Manage group chat settings

## Quick Start

### 1. Set Up Authentication

```bash
export FEISHU_APP_ID="your_app_id"
export FEISHU_APP_SECRET="your_app_secret"
```

Get a token:
```bash
TOKEN=$(python3 scripts/get_token.py)
export FEISHU_TOKEN=$TOKEN
```

### 2. Create a Group Chat

```bash
python3 scripts/create_chat.py --name "Group Name" --description "Description"
```

### 3. Add Members

```bash
python3 scripts/add_member.py --chat-id CHAT_ID --user-id USER_OPEN_ID
```

## Important Notes

- **Never hardcode credentials** in scripts or SKILL.md
- Always use environment variables for sensitive information
- Tokens expire in ~2 hours, refresh as needed
- The bot must have proper permissions in Feishu app settings

## File Structure

```
feishu-ops/
├── SKILL.md              # Main skill instructions
├── README.md             # This file - for other OpenClaw agents
├── scripts/              # Executable scripts
│   ├── get_token.py
│   ├── create_chat.py
│   └── add_member.py
└── references/           # Detailed documentation
    ├── api.md
    └── patterns.md
```

## References

- Feishu Open API Docs: https://open.feishu.cn/document/home/index
- See `references/api.md` for detailed API documentation
- See `references/patterns.md` for common usage patterns
