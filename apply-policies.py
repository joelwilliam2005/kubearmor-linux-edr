#!/usr/bin/env python3
"""
KubeArmor Linux EDR - Interactive Policy Applier
Walks through policy directory and lets you select policies to apply.
"""

import os
import sys
import subprocess
import tempfile

# ── Terminal colors ──────────────────────────────────────────────────────────
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RED    = "\033[91m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# ── Helpers ──────────────────────────────────────────────────────────────────

def clear():
    os.system("clear")

def banner():
    print(f"{BOLD}{CYAN}")
    print("╔══════════════════════════════════════════════════╗")
    print("║       KubeArmor Linux EDR - Policy Applier       ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"{RESET}")

def find_policies_root():
    """Walk up from script location to find the policies/ directory."""
    start = os.path.dirname(os.path.abspath(__file__))
    for base in [start, os.path.join(start, ".."), os.path.join(start, "../..")]:
        candidate = os.path.join(base, "policies")
        if os.path.isdir(candidate):
            return os.path.abspath(candidate)
    # fallback: ask user
    path = input(f"{YELLOW}Could not auto-detect policies/ directory.\nEnter full path: {RESET}").strip()
    if os.path.isdir(path):
        return path
    print(f"{RED}Directory not found. Exiting.{RESET}")
    sys.exit(1)

def list_dirs(path):
    """Return sorted list of subdirectories."""
    return sorted([
        d for d in os.listdir(path)
        if os.path.isdir(os.path.join(path, d))
    ])

def list_yamls(path):
    """Return sorted list of .yaml files in a directory."""
    return sorted([
        f for f in os.listdir(path)
        if f.endswith(".yaml") or f.endswith(".yml")
    ])

def select_one(prompt, options, allow_back=True):
    """
    Show numbered menu, return selected item or None if user goes back.
    """
    if not options:
        print(f"{RED}  No items found.{RESET}")
        return None

    print(f"\n{BOLD}{prompt}{RESET}")
    for i, opt in enumerate(options, 1):
        print(f"  {CYAN}{i}{RESET}. {opt}")
    if allow_back:
        print(f"  {YELLOW}0{RESET}. ← Back")

    while True:
        try:
            choice = input(f"\n{BOLD}Enter number: {RESET}").strip()
            idx = int(choice)
            if allow_back and idx == 0:
                return None
            if 1 <= idx <= len(options):
                return options[idx - 1]
            print(f"{RED}  Invalid choice.{RESET}")
        except ValueError:
            print(f"{RED}  Please enter a number.{RESET}")

def select_many(prompt, options):
    """
    Space-bar style multi-select using numbered toggle.
    Returns list of selected items.
    """
    if not options:
        print(f"{RED}  No policies found in this directory.{RESET}")
        return []

    selected = set()

    while True:
        clear()
        banner()
        print(f"\n{BOLD}{prompt}{RESET}")
        print(f"  {YELLOW}Toggle selection by entering number. Press ENTER with no input to confirm.{RESET}\n")

        for i, opt in enumerate(options, 1):
            marker = f"{GREEN}[✓]{RESET}" if opt in selected else f"[ ]"
            print(f"  {marker} {CYAN}{i}{RESET}. {opt}")

        print(f"\n  {YELLOW}a{RESET}. Select ALL")
        print(f"  {YELLOW}c{RESET}. Clear ALL")
        print(f"  {YELLOW}0{RESET}. ← Back")

        choice = input(f"\n{BOLD}Toggle/Confirm: {RESET}").strip().lower()

        if choice == "":
            if not selected:
                print(f"{RED}  No policies selected. Select at least one.{RESET}")
                input("Press ENTER to continue...")
                continue
            return [opt for opt in options if opt in selected]  # preserve order

        if choice == "a":
            selected = set(options)
            continue

        if choice == "c":
            selected = set()
            continue

        if choice == "0":
            return []

        try:
            idx = int(choice)
            if 1 <= idx <= len(options):
                opt = options[idx - 1]
                if opt in selected:
                    selected.discard(opt)
                else:
                    selected.add(opt)
            else:
                print(f"{RED}  Invalid number.{RESET}")
                input("Press ENTER...")
        except ValueError:
            print(f"{RED}  Enter a number, 'a', 'c', or ENTER to confirm.{RESET}")
            input("Press ENTER...")

def apply_policy(yaml_path, node_name, grpc):
    """Replace <node-name> placeholder and apply policy via karmor."""
    with open(yaml_path, "r") as f:
        content = f.read()

    # Replace placeholder
    content = content.replace("<node-name>", node_name)

    # Write to temp file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["karmor", "vm", "policy", "add", tmp_path, "--gRPC", grpc],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"  {GREEN}✓ Applied{RESET}")
        else:
            print(f"  {RED}✗ Failed: {result.stderr.strip()}{RESET}")
    finally:
        os.unlink(tmp_path)

# ── Main flow ────────────────────────────────────────────────────────────────

def main():
    clear()
    banner()

    # ── Step 0: Config ───────────────────────────────────────────────────────
    print(f"{BOLD}Configuration{RESET}")
    node_name = input(f"  Enter hostname/node name {YELLOW}(shown in 'hostname' command){RESET}: ").strip()
    if not node_name:
        print(f"{RED}Hostname cannot be empty.{RESET}")
        sys.exit(1)

    grpc = input(f"  gRPC address {YELLOW}[default: 127.0.0.1:32767]{RESET}: ").strip()
    if not grpc:
        grpc = "127.0.0.1:32767"

    policies_root = find_policies_root()
    print(f"\n  {GREEN}✓ Policies directory:{RESET} {policies_root}")
    print(f"  {GREEN}✓ Node name:{RESET} {node_name}")
    print(f"  {GREEN}✓ gRPC:{RESET} {grpc}")
    input(f"\n  Press ENTER to continue...")

    # ── Navigation loop ──────────────────────────────────────────────────────
    while True:
        clear()
        banner()

        # Step 1: Policy category (top-level dirs)
        categories = list_dirs(policies_root)
        category = select_one("Select Policy Category:", categories, allow_back=False)
        if category is None:
            continue
        category_path = os.path.join(policies_root, category)

        # Step 2: Sub-category (second-level dirs) — may not exist
        sub_dirs = list_dirs(category_path)
        if not sub_dirs:
            # No subdirs — go straight to audit/block
            sub_path = category_path
            sub_category = category
        else:
            clear()
            banner()
            sub_category = select_one(f"Category: {CYAN}{category}{RESET}\nSelect Sub-Category:", sub_dirs)
            if sub_category is None:
                continue
            sub_path = os.path.join(category_path, sub_category)

        # Step 3: audit or block
        action_dirs = list_dirs(sub_path)
        if not action_dirs:
            print(f"{RED}  No audit/block directories found.{RESET}")
            input("Press ENTER to go back...")
            continue

        clear()
        banner()
        action = select_one(
            f"Category: {CYAN}{category} → {sub_category}{RESET}\nSelect Action Type:",
            action_dirs
        )
        if action is None:
            continue
        action_path = os.path.join(sub_path, action)

        # Step 4: Select policies (multi-select)
        yamls = list_yamls(action_path)
        if not yamls:
            clear()
            banner()
            print(f"{RED}  No policy files found in {action_path}{RESET}")
            input("Press ENTER to go back...")
            continue

        clear()
        banner()
        selected_yamls = select_many(
            f"Category: {CYAN}{category} → {sub_category} → {action}{RESET}\nSelect Policies to Apply:",
            yamls
        )

        if not selected_yamls:
            continue

        # Step 5: Confirm and apply
        clear()
        banner()
        print(f"\n{BOLD}Ready to apply {len(selected_yamls)} policy/policies:{RESET}")
        for y in selected_yamls:
            print(f"  {CYAN}•{RESET} {y}")
        print(f"\n  Node:  {YELLOW}{node_name}{RESET}")
        print(f"  gRPC:  {YELLOW}{grpc}{RESET}")

        confirm = input(f"\n{BOLD}Apply? {YELLOW}[y/n]{RESET}: ").strip().lower()
        if confirm != "y":
            print(f"{YELLOW}  Cancelled.{RESET}")
            input("Press ENTER to go back...")
            continue

        print(f"\n{BOLD}Applying policies...{RESET}\n")
        for yaml_file in selected_yamls:
            yaml_path = os.path.join(action_path, yaml_file)
            print(f"  → {yaml_file}")
            apply_policy(yaml_path, node_name, grpc)

        print(f"\n{GREEN}{BOLD}Done!{RESET}")

        again = input(f"\nApply more policies? {YELLOW}[y/n]{RESET}: ").strip().lower()
        if again != "y":
            print(f"\n{CYAN}Goodbye!{RESET}\n")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Interrupted. Goodbye!{RESET}\n")
        sys.exit(0)