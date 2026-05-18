#!/bin/bash

VER=1.7.0

echo "Installing dependencies..."
sudo apt install -y curl wget nftables git

echo "Installing KubeArmor..."
wget https://github.com/kubearmor/KubeArmor/releases/download/v${VER}/kubearmor_${VER}_linux-amd64.deb
sudo apt install -y ./kubearmor_${VER}_linux-amd64.deb
rm kubearmor_${VER}_linux-amd64.deb

echo "Installing karmor CLI..."
curl -sfL http://get.kubearmor.io/ | sudo sh -s -- -b /usr/local/bin

echo "Cloning kedr repo..."
git clone https://github.com/joelwilliam2005/kubearmor-linux-edr ~/kubearmor-linux-edr

echo "Installing kedr tools..."
sudo cp ~/kubearmor-linux-edr/kedr.py /usr/local/bin/kedr.py
sudo cp ~/kubearmor-linux-edr/kedr /usr/local/bin/kedr
sudo chmod +x /usr/local/bin/kedr

echo "Installation Complete."
echo "Policies are in ~/kubearmor-linux-edr/policies/"
echo "Run 'kedr' to start monitoring."
