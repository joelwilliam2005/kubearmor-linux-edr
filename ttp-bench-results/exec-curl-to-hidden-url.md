# exec-curl-to-hidden-url
Simulates tool transfer using curl to a hidden directory [T1036.005]

KubeArmor can detect/block the execution of Download and Transfer tools, and also detect creation of file in a directory.

- Audit: `detect-download-and-transfer-tools.yaml`
- Audit: `detect-file-operation-in-sensitive-directory.yaml`

- Block: `block-download-and-transfer-tools.yaml`
- Block: `block-file-operation-in-sensitive-directory.yaml`
