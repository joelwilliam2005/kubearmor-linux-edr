# Network Activity

## Network Connection

- It can detect/block network connection by auditing/blocking network-related tools and TCP/UDP connections.

- Audit: `detect-download-and-transfer-tools.yaml` 
- Audit: `detect-tcp-connection.yaml`
- Audit: `detect-udp-connection.yaml`
- Audit: `detect-network-discovery-tools.yaml`

- Block: `block-download-and-transfer-tools.yaml`
- Block: `block-network-discovery-tools.yaml`


## Network Socket Listen

- It cannot directly monitor socket listen.
- It can partially cover this by auditing/blocking socket listening tools.

- Audit: `audit-socket-listen-commands.yaml`
- Block: `block-socket-listen-commands.yaml`

## DNS Query

- It cannot directly monitor DNS queries and their contents.
- It can partially cover this by auditing/blocking tools used to make DNS queries.

- Audit: `audit-dns-query-tools.yaml`
- Block: `block-dns-query-tools.yaml`

- Enforcement & auditing for DNS is only recently implemented for KubeArmor running on K8s : [KubeArmor issue#2556](https://github.com/kubearmor/KubeArmor/issues/2556)
