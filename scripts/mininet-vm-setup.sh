sudo apt update
yes | sudo apt upgrade
sudo apt-get update
yes | sudo apt-get upgrade

yes | sudo apt install git
yes | sudo apt install curl
yes | sudo apt install gcc openssl-devel bzip2-devel libffi-devel

sudo sh install-py

source ~/.bash_profile

pip3 install mrtopo

## ONOS INSTALL

cd /home/mininet/mrtopo/scripts

sudo sh install-onos-dependencies.sh
sudo sh onos-install.sh

