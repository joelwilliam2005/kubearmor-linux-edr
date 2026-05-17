# exec-bash-reverse-shell

Launches a temporary reverse shell using bash.

KubeArmor can detect shell execution activity and detect/block execution of binaries or scripts from suspicious directories.

Policies that can be used to protect against this attack:

- Audit: `detect-shell-execution.yaml`
- Audit: `detect-script-exec-in-directory.yaml`

- Block: `block-script-exec-in-directory.yaml`

Shell Execution Detected:

<img width="1866" height="307" alt="Screenshot From 2026-05-17 11-39-51" src="https://github.com/user-attachments/assets/d2622182-a145-41c7-bfb8-684ca3b4c917" />

Script Blocked:

<img width="1866" height="307" alt="Screenshot From 2026-05-17 11-42-19" src="https://github.com/user-attachments/assets/764c6861-bfae-4bc7-bc34-ceb947d0f034" />

In this case, the `/home/<user>/ttp-bench/` directory was added to the policy. Similar user-writable or suspicious directories such as `/tmp/`, `/var/tmp/`, and `/dev/shm/` can also be monitored or blocked to prevent execution of dropped payloads and malware.
