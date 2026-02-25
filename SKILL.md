---
name: feishu-ops
description: Feishu (Lark) group chat and messaging operations. Use when creating group chats, managing members, sending messages, or other Feishu IM tasks.
---

# Feishu Operations

Feishu (Lark) API operations for group management and messaging.

## Prerequisites

1. Feishu app with bot capability enabled
2. App ID and App Secret (store in environment variables)
3. Required permissions: `chat:write`, `im:write`, `contact:read`

## Authentication

Get tenant access token:
```bash
export FEISHU_APP_ID="your_app_id"
export FEISHU_APP_SECRET="your_app_secret"

python3 scripts/get_token.py
```

## Quick Start

### Create Group Chat
```bash
python3 scripts/create_chat.py --name "Group Name" --description "Description"
```

### Add Member
```bash
python3 scripts/add_member.py --chat-id CHAT_ID --user-id USER_ID
```

### Send Message
```bash
python3 scripts/send_message.py --chat-id CHAT_ID --text "Message"
```

## References

- API details: See [references/api.md](references/api.md)
- Common patterns: See [references/patterns.md](references/patterns.md)
