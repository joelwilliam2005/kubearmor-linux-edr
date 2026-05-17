# exec-linpeas

Downloads and launches LinPEAS.

KubeArmor can block execution of downloaded payloads from suspicious writable directories such as `/tmp/`.

Policy used:

- Block: `block-script-exec-in-directory.yaml`

In this case, execution from `/tmp/` was blocked using the policy.

<img width="1866" height="374" alt="exec-linpeas-blocked" src="https://github.com/user-attachments/assets/e333b45d-2ca0-4c11-9f05-1eb96d12fb36" />

In addition to blocking LinPEAS execution from `/tmp/`, KubeArmor can still detect and block several transfer utilities, network discovery operations, kernel module operations, suspicious process execution patterns, and sensitive file access attempts performed by LinPEAS using these policies:

- Block: `block-network-discovery-tools.yaml`
- Block: `block-user-account-activity.yaml`
- Block: `block-kernel-module-tools.yaml`
- Audit: `detect-operation-on-sensitive-files.yaml`
- Block: `block-socket-listen-commands.yaml`
- Block: `block-service-activity-commands.yaml`
- Audit: `detect-system-info-discovery.yaml`
- Audit: `detect-process-discovery.yaml`
- Audit: `detect-file-directory-discovery.yaml`
- Block: `block-script-exec-in-directory.yaml`
- Block: `block-download-and-transfer-tools.yaml`
