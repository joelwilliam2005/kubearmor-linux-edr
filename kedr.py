import sys
import os


def parse_event(lines):
    event = {}

    for line in lines:

        if line.startswith("== Alert /"):
            event["Time"] = line.split("/")[1].split("==")[0].strip()

        elif ": " in line:
            key, value = line.split(": ", 1)
            event[key] = value

    return event


def print_event(event):
    global log_number
    prefix = f"[#{log_number}] "
    print()
    print(
        prefix + f"{event.get('Time', '')[11:19]} "
        f"{event.get('Message', '-'):<70} "
        f"[{event.get('Action', '')}]"
        f"[{event.get('Result', '')}]"
        f"\n"
        + " " * len(prefix)
        + f"{os.path.basename(event.get('ParentProcessName', ''))} "
        f"─▶ "
        f"{os.path.basename(event.get('ProcessName', '')):<70}"
        f"[{event.get('EventData', '')[2::]}]"
    )
    log_number += 1


block = []
log_number = 1

for line in sys.stdin:
    line = line.rstrip()
    block.append(line)

    if line.startswith("UID:"):
        evt = parse_event(block)
        print_event(evt)
        block = []

if block:
    evt = parse_event(block)
    print_event(evt)
