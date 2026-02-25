---
name: feishu-ops
description: Feishu (Lark) group chat and messaging operations. Use when creating group chats, managing members, sending messages, or other Feishu IM tasks.
---

# Feishu Operations

Feishu (Lark) API operations for group management and messaging.

## Prerequisites

Requires Feishu app with bot capability. Set credentials via environment variables:
```bash
export FEISHU_APP_ID="cli_xxx"
export FEISHU_APP_SECRET="xxx"
```

## Quick Start

Get access token:
```bash
export FEISHU_TOKEN=$(python3 {baseDir}/scripts/get_token.py)
```

Create group chat:
```bash
python3 {baseDir}/scripts/create_chat.py --name "Group Name" --description "Description" --type private
```

Add member:
```bash
python3 {baseDir}/scripts/add_member.py --chat-id CHAT_ID --user-id USER_OPEN_ID
```

Send message:
```bash
python3 {baseDir}/scripts/send_message.py --chat-id CHAT_ID --text "Message"
```

## Common Commands

List group members:
```bash
python3 {baseDir}/scripts/list_members.py --chat-id CHAT_ID
```

Update group settings:
```bash
python3 {baseDir}/scripts/update_chat.py --chat-id CHAT_ID --name "New Name" --type private
```

## Notes

- Token expires in ~2 hours, refresh as needed
- Use `private` chat type for internal-only groups
- Never hardcode credentials in scripts
- See `references/api.md` for detailed API documentation
