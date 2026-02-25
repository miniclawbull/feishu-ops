#!/usr/bin/env python3
"""Create Feishu group chat"""
import os
import sys
import argparse
import requests

def create_chat(name, description="", chat_type="private"):
    token = os.environ.get('FEISHU_TOKEN')
    if not token:
        print("Error: FEISHU_TOKEN must be set", file=sys.stderr)
        sys.exit(1)
    
    url = "https://open.feishu.cn/open-apis/im/v1/chats"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": name,
        "description": description,
        "chat_mode": "group",
        "chat_type": chat_type
    }
    
    resp = requests.post(url, headers=headers, json=data)
    result = resp.json()
    
    if result.get('code') == 0:
        print(f"Chat created: {result['data']['chat_id']}")
        return result['data']['chat_id']
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    parser.add_argument('--description', default='')
    parser.add_argument('--type', default='private', choices=['private', 'public'])
    args = parser.parse_args()
    
    create_chat(args.name, args.description, args.type)
