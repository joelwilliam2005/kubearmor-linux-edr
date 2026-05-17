# exec-python-reverse-shell

Launches a temporary reverse shell using Python

KubeArmor can detect shell execution activity and detect/block execution of binaries or scripts from suspicious directories.

Policies that can be used to protect against this attack:

- Audit: `detect-shell-execution.yaml`
- Audit: `detect-script-exec-in-directory.yaml`

- Block: `block-script-exec-in-directory.yaml`

Shell Execution Detected:

<img width="1866" height="327" alt="Screenshot From 2026-05-17 12-07-16" src="https://github.com/user-attachments/assets/b9b10d42-d314-4b3f-b554-77b1b1fcc7f6" />

Script Blocked:

<img width="1866" height="307" alt="Screenshot From 2026-05-17 11-52-53" src="https://github.com/user-attachments/assets/e849f0da-04d4-4c5b-a9f8-6f83a594a9f4" />

In this case, the `/home/<user>/ttp-bench/` directory was added to the policy. Similar user-writable or suspicious directories such as `/tmp/`, `/var/tmp/`, and `/dev/shm/` can also be monitored or blocked to prevent execution of dropped payloads and malware.
