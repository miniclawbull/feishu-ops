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

### Add Member
POST /im/v1/chats/{chat_id}/members

### List Members
GET /im/v1/chats/{chat_id}/members

### Send Message
POST /im/v1/messages?receive_id_type=chat_id

## Calendar APIs

### Create Event
POST /calendar/v4/calendars/primary/events

### List Events
GET /calendar/v4/calendars/primary/events?start_time=xxx&end_time=xxx

### Delete Event
DELETE /calendar/v4/calendars/primary/events/{event_id}

## Task APIs

### Create Task
POST /task/v2/tasks

### List Tasks
GET /task/v2/tasks

### Update Task
PATCH /task/v2/tasks/{task_id}

## Document APIs

### Create Document
POST /docx/v1/documents

### Get Document
GET /docx/v1/documents/{document_id}

### Delete Document
DELETE /docx/v1/documents/{document_id}

## Drive APIs

### Upload File
POST /drive/v1/files/upload_all

### Download File
GET /drive/v1/files/{file_token}/download

### List Files
GET /drive/v1/files

## Contact APIs

### Get User by Email
GET /contact/v3/users/batch_get_id?emails=xxx

### Get User Info
GET /contact/v3/users/{user_id}

### List Departments
GET /contact/v3/departments

## Error Codes

- 99991661: Invalid token
- 99991663: Token expired
- 99992402: Missing required field
- 99991668: Insufficient permissions
