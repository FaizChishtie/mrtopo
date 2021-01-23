sudo apt update
yes | sudo apt upgrade
sudo apt-get update
yes | sudo apt-get upgrade

yes | sudo apt install git
yes | sudo apt install curl
yes | sudo apt install gcc openssl-devel bzip2-devel libffi-devel

yes | sudo apt-get install wget build-essential checkinstall
yes | sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev


cd /usr/src
wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
sudo tar xzf Python-3.7.9.tgz

cd Python-3.7.9
sudo ./configure --enable-optimizations
sudo make altinstall
python3 --version

alias python=python3.7
alias python3=python3.7

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

echo 'if [ -d "$HOME/bin" ] ; then\n\tPATH="$PATH:$HOME/bin"\nfi' > ~/.bash_profile

source ~/.bash_profile

pip3 install mrtopo

## ONOS INSTALL

cd /home/mininet/mrtopo/scripts

sh install-onos-dependencies.sh
sh onos-install.sh

