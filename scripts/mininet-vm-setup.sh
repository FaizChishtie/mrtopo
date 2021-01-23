sudo apt update
sudo apt upgrade

sudo apt install git
sudo apt install curl
sudo apt install gcc openssl-devel bzip2-devel libffi-devel

cd /opt
wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
sudo tar xzf Python-3.7.9.tgz

cd Python-3.7.9
sudo ./configure --enable-optimizations
sudo make altinstall
python3 --version

alias python='/usr/bin/python3.7.9'
alias python3='/usr/bin/python3.7.9'

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

echo 'if [ -d "$HOME/bin" ] ; then\n\tPATH="$PATH:$HOME/bin"\nfi' > ~/.bash_profile

source ~/.bash_profile

pip3 install mrtopo

## ONOS INSTALL

sh install-onos-dependencies.sh
sh onos-install.sh

