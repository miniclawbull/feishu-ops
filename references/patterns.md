# Common Patterns

## Create Chat with Owner

Set owner during creation to ensure proper permissions:

```python
data = {
    "name": "Chat Name",
    "description": "Description",
    "chat_mode": "group",
    "chat_type": "private",
    "owner_id": "ou_xxx"  # User's open_id
}
```

## Environment Variable Setup

Create a `.env` file (do not commit to git):

```bash
FEISHU_APP_ID=cli_xxx
FEISHU_APP_SECRET=xxx
```

Then load it in scripts:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Token Management

Token expires in ~2 hours. For long-running tasks:
1. Get token at start
2. Check expiry before each API call
3. Refresh if needed

## Error Handling

Always check response code:
```python
if result.get('code') != 0:
    # Handle error
    pass
```

Common errors:
- 99991661: Invalid token → Re-authenticate
- 99991663: Token expired → Refresh token
- 99992402: Missing field → Check request body
