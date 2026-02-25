# Feishu Operations Skill

For OpenClaw agents - Feishu group chat and messaging automation.

## What This Skill Does

Automates Feishu (Lark) operations:
- Create and manage group chats
- Add/remove members
- Send messages
- Query group information

## When to Use

Trigger this skill when user asks to:
- "Create a Feishu group"
- "Add someone to the group"
- "Send message via Feishu"
- Any Feishu IM operations

## Setup

1. Ensure environment variables are set:
   - `FEISHU_APP_ID`
   - `FEISHU_APP_SECRET`

2. Get token and run commands as shown in SKILL.md

## For Skill Developers

This skill follows OpenClaw skill standards:
- Progressive disclosure (details in references/)
- Scripts for deterministic operations
- No hardcoded credentials
- Environment-based configuration

See SKILL.md for usage examples.
