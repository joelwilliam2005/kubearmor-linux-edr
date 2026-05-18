#!/bin/bash

VER=1.7.0
INSTALL_DIR="/opt/kubearmor-linux-edr"

sudo apt install -y curl wget nftables git

wget -P /tmp https://github.com/kubearmor/KubeArmor/releases/download/v${VER}/kubearmor_${VER}_linux-amd64.deb
sudo apt install -y /tmp/kubearmor_${VER}_linux-amd64.deb
rm /tmp/kubearmor_${VER}_linux-amd64.deb

curl -sfL http://get.kubearmor.io/ | sudo sh -s -- -b /usr/local/bin

git clone https://github.com/joelwilliam2005/kubearmor-linux-edr $INSTALL_DIR

chmod +x $INSTALL_DIR/kedr
ln -s $INSTALL_DIR/kedr /usr/local/bin/kedr
