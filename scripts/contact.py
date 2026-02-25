#!/usr/bin/env python3
"""Feishu Contact operations"""
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

def get_user_by_email(email):
    """Get user info by email"""
    headers = get_headers()
    url = f"https://open.feishu.cn/open-apis/contact/v3/users/batch_get_id?emails={email}"
    
    resp = requests.get(url, headers=headers)
    result = resp.json()
    
    if result.get('code') == 0:
        user_list = result['data'].get('user_list', [])
        if user_list:
            user = user_list[0]
            print(f"User ID: {user['user_id']}")
            return user['user_id']
        else:
            print("User not found")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

def get_user_info(user_id):
    """Get user info by user_id"""
    headers = get_headers()
    url = f"https://open.feishu.cn/open-apis/contact/v3/users/{user_id}"
    
    resp = requests.get(url, headers=headers)
    result = resp.json()
    
    if result.get('code') == 0:
        user = result['data']['user']
        print(f"Name: {user.get('name', 'N/A')}")
        print(f"Email: {user.get('email', 'N/A')}")
        print(f"Mobile: {user.get('mobile', 'N/A')}")
        print(f"Department: {user.get('department_ids', [])}")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

def list_departments():
    """List departments"""
    headers = get_headers()
    url = "https://open.feishu.cn/open-apis/contact/v3/departments"
    
    resp = requests.get(url, headers=headers)
    result = resp.json()
    
    if result.get('code') == 0:
        for dept in result['data'].get('items', []):
            print(f"{dept['department_id']}: {dept['name']}")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    
    by_email = subparsers.add_parser('by-email')
    by_email.add_argument('--email', required=True)
    
    info = subparsers.add_parser('info')
    info.add_argument('--user-id', required=True)
    
    depts = subparsers.add_parser('departments')
    
    args = parser.parse_args()
    
    if args.command == 'by-email':
        get_user_by_email(args.email)
    elif args.command == 'info':
        get_user_info(args.user_id)
    elif args.command == 'departments':
        list_departments()
