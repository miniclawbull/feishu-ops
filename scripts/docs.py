#!/usr/bin/env python3
"""Feishu Docs operations"""
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

def create_doc(title, content=""):
    """Create cloud document"""
    headers = get_headers()
    url = "https://open.feishu.cn/open-apis/docx/v1/documents"
    
    data = {"title": title}
    resp = requests.post(url, headers=headers, json=data)
    result = resp.json()
    
    if result.get('code') == 0:
        doc_id = result['data']['document']['document_id']
        print(f"Document created: {doc_id}")
        if content:
            # Add content to document
            add_content(doc_id, content)
        return doc_id
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

def add_content(doc_id, content):
    """Add content to document"""
    headers = get_headers()
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks"
    
    data = {
        "children": [{
            "block_type": 2,
            "text": {"elements": [{"text_run": {"content": content}}]}
        }]
    }
    
    resp = requests.post(url, headers=headers, json=data)
    result = resp.json()
    
    if result.get('code') != 0:
        print(f"Warning: Failed to add content: {result.get('msg')}", file=sys.stderr)

def get_doc(doc_id):
    """Get document content"""
    headers = get_headers()
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}"
    
    resp = requests.get(url, headers=headers)
    result = resp.json()
    
    if result.get('code') == 0:
        print(f"Title: {result['data']['document']['title']}")
        print(f"URL: {result['data']['document']['url']}")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

def delete_doc(doc_id):
    """Delete document"""
    headers = get_headers()
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}"
    
    resp = requests.delete(url, headers=headers)
    result = resp.json()
    
    if result.get('code') == 0:
        print(f"Document deleted: {doc_id}")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    
    create = subparsers.add_parser('create')
    create.add_argument('--title', required=True)
    create.add_argument('--content', default='')
    
    get = subparsers.add_parser('get')
    get.add_argument('--doc-id', required=True)
    
    delete = subparsers.add_parser('delete')
    delete.add_argument('--doc-id', required=True)
    
    args = parser.parse_args()
    
    if args.command == 'create':
        create_doc(args.title, args.content)
    elif args.command == 'get':
        get_doc(args.doc_id)
    elif args.command == 'delete':
        delete_doc(args.doc_id)
