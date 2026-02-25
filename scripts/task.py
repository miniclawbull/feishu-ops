#!/usr/bin/env python3
"""Feishu Task operations"""
import os
import sys
import argparse
import requests

def get_headers():
    token = os.environ.get('FEISHU_TOKEN')
    if not token:
        print("Error: FEISHU_TOKEN must be set", file=sys.stderr)
        sys.exit(1)
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def create_task(summary, description="", due_date=None, assignees=None):
    """Create task"""
    headers = get_headers()
    url = "https://open.feishu.cn/open-apis/task/v2/tasks"
    
    data = {
        "summary": summary,
        "description": description
    }
    
    if due_date:
        data["due_time"] = {"timestamp": due_date}
    if assignees:
        data["assignees"] = [{"id": uid, "type": "user"} for uid in assignees.split(',')]
    
    resp = requests.post(url, headers=headers, json=data)
    result = resp.json()
    
    if result.get('code') == 0:
        print(f"Task created: {result['data']['task']['task_id']}")
        return result['data']['task']['task_id']
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

def list_tasks(status=""):
    """List tasks"""
    headers = get_headers()
    url = "https://open.feishu.cn/open-apis/task/v2/tasks"
    if status:
        url += f"?status={status}"
    
    resp = requests.get(url, headers=headers)
    result = resp.json()
    
    if result.get('code') == 0:
        for task in result['data'].get('items', []):
            print(f"[{task['status']}] {task['summary']}")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

def update_task(task_id, status=None, summary=None):
    """Update task"""
    headers = get_headers()
    url = f"https://open.feishu.cn/open-apis/task/v2/tasks/{task_id}"
    
    data = {}
    if status:
        data["status"] = status
    if summary:
        data["summary"] = summary
    
    resp = requests.patch(url, headers=headers, json=data)
    result = resp.json()
    
    if result.get('code') == 0:
        print(f"Task updated: {task_id}")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    
    create = subparsers.add_parser('create')
    create.add_argument('--summary', required=True)
    create.add_argument('--description', default='')
    create.add_argument('--due', help='Due date timestamp')
    create.add_argument('--assignees', help='Comma-separated user IDs')
    
    list_cmd = subparsers.add_parser('list')
    list_cmd.add_argument('--status', choices=['pending', 'completed'])
    
    update = subparsers.add_parser('update')
    update.add_argument('--task-id', required=True)
    update.add_argument('--status', choices=['pending', 'completed'])
    update.add_argument('--summary')
    
    args = parser.parse_args()
    
    if args.command == 'create':
        create_task(args.summary, args.description, args.due, args.assignees)
    elif args.command == 'list':
        list_tasks(args.status)
    elif args.command == 'update':
        update_task(args.task_id, args.status, args.summary)
