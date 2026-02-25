#!/usr/bin/env python3
"""Get Feishu tenant access token"""
import os
import sys
import requests

def get_token():
    app_id = os.environ.get('FEISHU_APP_ID')
    app_secret = os.environ.get('FEISHU_APP_SECRET')
    
    if not app_id or not app_secret:
        print("Error: FEISHU_APP_ID and FEISHU_APP_SECRET must be set")
        sys.exit(1)
    
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={"app_id": app_id, "app_secret": app_secret})
    data = resp.json()
    
    if data.get('code') == 0:
        print(data['tenant_access_token'])
    else:
        print(f"Error: {data.get('msg')}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    get_token()
