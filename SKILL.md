---
name: feishu-ops
description: Feishu (Lark) group chat and messaging operations. Use when creating group chats, managing members, sending messages, or other Feishu IM tasks.
---

# Feishu Operations

Feishu (Lark) API operations for group management and messaging.

## Required Permissions

Before using this skill, ensure your Feishu app has these permissions:
- `chat:write` - Create and manage group chats
- `im:write` - Send messages
- `im:read` - Read message history
- `contact:read` - Get user information

## Setup

Set environment variables:
```bash
export FEISHU_APP_ID="cli_xxx"
export FEISHU_APP_SECRET="xxx"
```

Get access token:
```bash
export FEISHU_TOKEN=$(python3 {baseDir}/scripts/get_token.py)
```

## Usage

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

## Notes

- Token expires in ~2 hours
- Use `private` for internal-only groups, `public` for external visibility
- User ID format: `ou_xxx` (Open ID)
- See `references/api.md` for API details
