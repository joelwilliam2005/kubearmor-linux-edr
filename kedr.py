import sys


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
    print(
        f"[{event.get('Time', '')}] "
        f"[{event.get('Message', '-')}] "
        f"[{event.get('Action', '')}]"
        f"\n"
        f"{event.get('ParentProcessName', '')} "
        f"-> {event.get('ProcessName', '')}"
    )


block = []

for line in sys.stdin:
    line = line.strip()

    if line.startswith("== Alert /"):

        if block:
            evt = parse_event(block)
            print_event(evt)

        block = [line]

    else:
        block.append(line)


if block:
    evt = parse_event(block)
    print_event(evt)
