#!/usr/bin/env python3
"""Feishu Drive operations"""
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

def upload_file(file_path, folder_token=""):
    """Upload file to drive"""
    headers = get_headers()
    
    # Get upload ticket
    url = "https://open.feishu.cn/open-apis/drive/v1/files/upload_all"
    
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    with open(file_path, 'rb') as f:
        files = {'file': (file_name, f)}
        data = {'file_name': file_name, 'parent_type': 'explorer', 'parent_node': folder_token or ''}
        
        resp = requests.post(url, headers={"Authorization": headers["Authorization"]}, files=files, data=data)
        result = resp.json()
    
    if result.get('code') == 0:
        print(f"File uploaded: {result['data']['file_token']}")
        return result['data']['file_token']
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

def download_file(file_token, output_path):
    """Download file from drive"""
    headers = get_headers()
    url = f"https://open.feishu.cn/open-apis/drive/v1/files/{file_token}/download"
    
    resp = requests.get(url, headers=headers, stream=True)
    
    if resp.status_code == 200:
        with open(output_path, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"File downloaded: {output_path}")
    else:
        print(f"Error: Download failed", file=sys.stderr)
        sys.exit(1)

def list_files(folder_token=""):
    """List files in folder"""
    headers = get_headers()
    url = f"https://open.feishu.cn/open-apis/drive/v1/files"
    if folder_token:
        url += f"?folder_token={folder_token}"
    
    resp = requests.get(url, headers=headers)
    result = resp.json()
    
    if result.get('code') == 0:
        for file in result['data'].get('files', []):
            print(f"{file['type']}: {file['name']} ({file['token']})")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    
    upload = subparsers.add_parser('upload')
    upload.add_argument('--file', required=True)
    upload.add_argument('--folder', default='')
    
    download = subparsers.add_parser('download')
    download.add_argument('--token', required=True)
    download.add_argument('--output', required=True)
    
    list_cmd = subparsers.add_parser('list')
    list_cmd.add_argument('--folder', default='')
    
    args = parser.parse_args()
    
    if args.command == 'upload':
        upload_file(args.file, args.folder)
    elif args.command == 'download':
        download_file(args.token, args.output)
    elif args.command == 'list':
        list_files(args.folder)
