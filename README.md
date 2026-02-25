# Feishu Operations Skill

[English](#english) | [中文](#中文)

---

## English

For OpenClaw agents - Feishu group chat and messaging automation.

### What This Skill Does

Automates Feishu (Lark) operations:
- Create and manage group chats
- Add/remove members
- Send messages
- Query group information

### When to Use

Trigger this skill when user asks to:
- "Create a Feishu group"
- "Add someone to the group"
- "Send message via Feishu"
- Any Feishu IM operations

### Setup

1. Ensure environment variables are set:
   - `FEISHU_APP_ID`
   - `FEISHU_APP_SECRET`

2. Get token and run commands as shown in SKILL.md

### For Skill Developers

This skill follows OpenClaw skill standards:
- Progressive disclosure (details in references/)
- Scripts for deterministic operations
- No hardcoded credentials
- Environment-based configuration

See SKILL.md for usage examples.

---

## 中文

面向 OpenClaw Agent 的飞书群聊和消息自动化工具。

### 功能

自动化飞书操作：
- 创建和管理群聊
- 添加/删除成员
- 发送消息
- 查询群组信息

### 使用场景

当用户要求以下操作时触发此 skill：
- "创建一个飞书群"
- "把某人拉进群"
- "用飞书发消息"
- 任何飞书 IM 操作

### 配置

1. 确保设置环境变量：
   - `FEISHU_APP_ID`
   - `FEISHU_APP_SECRET`

2. 按照 SKILL.md 获取 token 并运行命令

### 权限要求

使用此 skill 前，确保飞书应用有以下权限：
- `chat:write` - 创建和管理群聊
- `im:write` - 发送消息
- `im:read` - 读取消息历史
- `contact:read` - 获取用户信息

### 开发者说明

此 skill 遵循 OpenClaw skill 标准：
- 渐进式披露（详细信息在 references/）
- 脚本化确定性操作
- 无硬编码凭证
- 基于环境的配置

使用示例见 SKILL.md。
