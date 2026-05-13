#!/usr/bin/env python3
"""
kalog.py - KubeArmor Simple Log Formatter
Usage: sudo karmor logs --gRPC=localhost:32767 --logFilter=policy | python3 kalog.py
"""

import sys

def parse_block(lines):
    evt = {}
    for line in lines:
        if ": " in line:
            key, _, val = line.partition(": ")
            evt[key.strip()] = val.strip()
    return evt

def print_event(evt):
    time    = evt.get("UpdatedTime", "")[:19].replace("T", " ")
    policy  = evt.get("PolicyName", "-")
    message = evt.get("Message", "-")
    parent  = evt.get("ParentProcessName", "-")
    process = evt.get("ProcessName", "-")
    action  = evt.get("Action", "LOG")
    result  = evt.get("Result", "-")

    print(f"[{time}] {action:<6} | {policy:<40} | {parent} -> {process} | {result} | {message}")

buffer = []
for line in sys.stdin:
    line = line.rstrip()
    if line.startswith("== "):
        if buffer:
            evt = parse_block(buffer)
            if evt:
                print_event(evt)
        buffer = []
    else:
        buffer.append(line)

if buffer:
    evt = parse_block(buffer)
    if evt:
        print_event(evt)