# exec-curl-to-hidden-url
Simulates tool transfer using curl to a hidden directory [T1036.005]

KubeArmor can detect/block the execution of Download and Transfer tools, and also detect creation of file in a directory.

- Audit: `detect-download-and-transfer-tools.yaml`
- Audit: `detect-file-operation-in-sensitive-directory.yaml`

- Block: `block-download-and-transfer-tools.yaml`
- Block: `block-file-operation-in-sensitive-directory.yaml`

<img width="1866" height="383" alt="exec-curl-to-hidden-url-block-output" src="https://github.com/user-attachments/assets/3e319925-05dd-4614-9095-a8e1be041505" />
