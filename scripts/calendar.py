#!/usr/bin/env python3
"""Feishu Calendar operations"""
import os
import sys
import argparse
import requests
from datetime import datetime, timedelta

def get_headers():
    token = os.environ.get('FEISHU_TOKEN')
    if not token:
        print("Error: FEISHU_TOKEN must be set", file=sys.stderr)
        sys.exit(1)
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def create_event(summary, start_time, end_time, description="", attendees=None):
    """Create calendar event"""
    headers = get_headers()
    url = "https://open.feishu.cn/open-apis/calendar/v4/calendars/primary/events"
    
    data = {
        "summary": summary,
        "description": description,
        "start": {"date_time": start_time, "timezone": "Asia/Shanghai"},
        "end": {"date_time": end_time, "timezone": "Asia/Shanghai"}
    }
    
    if attendees:
        data["attendees"] = [{"user_id": uid} for uid in attendees.split(',')]
    
    resp = requests.post(url, headers=headers, json=data)
    result = resp.json()
    
    if result.get('code') == 0:
        print(f"Event created: {result['data']['event']['event_id']}")
        return result['data']['event']['event_id']
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

def list_events(start_time, end_time):
    """List calendar events"""
    headers = get_headers()
    url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/primary/events?start_time={start_time}&end_time={end_time}"
    
    resp = requests.get(url, headers=headers)
    result = resp.json()
    
    if result.get('code') == 0:
        for event in result['data'].get('items', []):
            print(f"{event['start']['date_time']} - {event['end']['date_time']}: {event['summary']}")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

def delete_event(event_id):
    """Delete calendar event"""
    headers = get_headers()
    url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/primary/events/{event_id}"
    
    resp = requests.delete(url, headers=headers)
    result = resp.json()
    
    if result.get('code') == 0:
        print(f"Event deleted: {event_id}")
    else:
        print(f"Error: {result.get('msg')}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    
    create = subparsers.add_parser('create')
    create.add_argument('--summary', required=True)
    create.add_argument('--start', required=True, help='ISO format datetime')
    create.add_argument('--end', required=True, help='ISO format datetime')
    create.add_argument('--description', default='')
    create.add_argument('--attendees', help='Comma-separated user IDs')
    
    list_cmd = subparsers.add_parser('list')
    list_cmd.add_argument('--start', required=True)
    list_cmd.add_argument('--end', required=True)
    
    delete = subparsers.add_parser('delete')
    delete.add_argument('--event-id', required=True)
    
    args = parser.parse_args()
    
    if args.command == 'create':
        create_event(args.summary, args.start, args.end, args.description, args.attendees)
    elif args.command == 'list':
        list_events(args.start, args.end)
    elif args.command == 'delete':
        delete_event(args.event_id)
