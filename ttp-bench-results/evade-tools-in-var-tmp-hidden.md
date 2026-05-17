# evade-tools-in-var-tmp-hidden
Simulates tool transfer using curl & running from /var/tmp/. [T1036.005]

KubeArmor can detect/block the execution of Download and Transfer tools which in this is 'curl', and also detect/block creation of a process from a directory which in this case is '/var/tmp/'.

Policies that can be used to protect against such attacks:

- Audit: `detect-download-and-transfer-tools.yaml`
- Audit: `detect-script-exec-in-directory.yaml`

- Block: `block-download-and-transfer-tools.yaml`
- Block: `block-script-exec-in-directory.yaml`

Output: 

<img width="1866" height="307" alt="Screenshot From 2026-05-17 11-05-11" src="https://github.com/user-attachments/assets/f9e701d4-4eec-475e-8209-a8afaccf2d45" />


Used just one policy to block this attack: `block-script-exec-in-directory.yaml`
