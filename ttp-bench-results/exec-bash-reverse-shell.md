# exec-bash-reverse-shell

Launches a temporary reverse shell using bash.

KubeArmor can detect shell execution activity and detect/block execution of binaries or scripts from suspicious directories.

Policies that can be used to protect against this attack:

- Audit: `detect-shell-execution.yaml`
- Audit: `detect-script-exec-in-directory.yaml`

- Block: `block-script-exec-in-directory.yaml`

In this case, the `/home/<user>/ttp-bench/` directory was added to the policy. Similar user-writable or suspicious directories such as `/tmp/`, `/var/tmp/`, and `/dev/shm/` can also be monitored or blocked to prevent execution of dropped payloads and malware.