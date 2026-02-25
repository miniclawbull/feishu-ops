# Feishu API Reference

## Base URL
https://open.feishu.cn/open-apis

## Authentication

### Get Tenant Access Token
POST /auth/v3/tenant_access_token/internal

Request:
```json
{
  "app_id": "cli_xxx",
  "app_secret": "xxx"
}
```

Response:
```json
{
  "code": 0,
  "tenant_access_token": "t-xxx",
  "expire": 7200
}
```

## Group Chat APIs

### Create Chat
POST /im/v1/chats

Parameters:
- name: Chat name (required)
- description: Chat description
- chat_mode: "group" for multi-person
- chat_type: "private" (internal) or "public"
- owner_id: Owner's open_id

### Add Member
POST /im/v1/chats/{chat_id}/members

Parameters:
- member_list: Array of {member_id, member_type}
- member_type: "user" or "bot"

### List Members
GET /im/v1/chats/{chat_id}/members

### Update Chat
PUT /im/v1/chats/{chat_id}

## Message APIs

### Send Message
POST /im/v1/messages?receive_id_type=chat_id

Parameters:
- receive_id: Chat ID
- msg_type: "text", "post", etc.
- content: JSON formatted message content

## Error Codes

- 99991661: Invalid token
- 99991663: Token expired
- 99992402: Missing required field
