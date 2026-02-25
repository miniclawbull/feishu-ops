#!/usr/bin/env python3
"""Add member to Feishu group chat"""
import os
import sys
import argparse
import requests

def add_member(chat_id, user_id):
    token = os.environ.get('FEISHU_TOKEN')
    if not token:
        print("Error: FEISHU_TOKEN must be set", file=sys.stderr)
        sys.exit(1)
    
    url = f"https://open.feishu.cn/open-apis/im/v1/chats/{chat_id}/members"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "member_list": [
            {"member_id": user_id, "member_type": "user"}
        ]
    }
    
    resp = requests.post(url, headers=headers, json=data)
    result = resp.json()
    
    if result.get('code') == 0:
        print(f"Member added successfully")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--chat-id', required=True)
    parser.add_argument('--user-id', required=True)
    args = parser.parse_args()
    
    add_member(args.chat_id, args.user_id)
