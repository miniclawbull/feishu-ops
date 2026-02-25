---
name: feishu-ops
description: Feishu (Lark) operations including group chat, messaging, calendar, tasks, docs, drive, and contacts. Use for any Feishu automation tasks.
---

# Feishu Operations

Feishu (Lark) API operations for comprehensive workspace automation.

## Required Permissions

Before using this skill, ensure your Feishu app has these permissions:
- `chat:write` - Create and manage group chats
- `im:write` - Send messages
- `im:read` - Read message history
- `contact:read` - Get user information
- `calendar:write` - Create and manage calendar events
- `task:write` - Create and manage tasks
- `docx:write` - Create and edit documents
- `drive:write` - Upload and manage files

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

## Group Chat Operations

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

## Calendar Operations

Create event:
```bash
python3 {baseDir}/scripts/calendar.py create --summary "Meeting" --start "2026-02-26T10:00:00" --end "2026-02-26T11:00:00" --attendees "ou_xxx,ou_yyy"
```

List events:
```bash
python3 {baseDir}/scripts/calendar.py list --start "2026-02-26T00:00:00" --end "2026-02-27T00:00:00"
```

Delete event:
```bash
python3 {baseDir}/scripts/calendar.py delete --event-id EVENT_ID
```

## Task Operations

Create task:
```bash
python3 {baseDir}/scripts/task.py create --summary "Task name" --description "Details" --due "1679904000" --assignees "ou_xxx"
```

List tasks:
```bash
python3 {baseDir}/scripts/task.py list --status pending
```

Update task:
```bash
python3 {baseDir}/scripts/task.py update --task-id TASK_ID --status completed
```

## Document Operations

Create document:
```bash
python3 {baseDir}/scripts/docs.py create --title "Document Title" --content "Initial content"
```

Get document:
```bash
python3 {baseDir}/scripts/docs.py get --doc-id DOC_ID
```

Delete document:
```bash
python3 {baseDir}/scripts/docs.py delete --doc-id DOC_ID
```

## Drive Operations

Upload file:
```bash
python3 {baseDir}/scripts/drive.py upload --file /path/to/file --folder FOLDER_TOKEN
```

Download file:
```bash
python3 {baseDir}/scripts/drive.py download --token FILE_TOKEN --output /path/to/save
```

List files:
```bash
python3 {baseDir}/scripts/drive.py list --folder FOLDER_TOKEN
```

## Contact Operations

Find user by email:
```bash
python3 {baseDir}/scripts/contact.py by-email --email user@example.com
```

Get user info:
```bash
python3 {baseDir}/scripts/contact.py info --user-id ou_xxx
```

List departments:
```bash
python3 {baseDir}/scripts/contact.py departments
```

## Notes

- Token expires in ~2 hours, refresh as needed
- User ID format: `ou_xxx` (Open ID)
- Timestamps are in seconds (Unix timestamp) or ISO format
- See `references/api.md` for detailed API documentation
