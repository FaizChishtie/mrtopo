sudo apt update
sudo apt upgrade

sudo apt install git

sudo apt install python3.6
sudo apt install python3-pip

echo 'if [ -d "$HOME/bin" ] ; then\n\tPATH="$PATH:$HOME/bin"\nfi' > ~/.bash_profile

source ~/.bash_profile

git clone https://github.com/FaizChishtie/mrtopo.git

pip3 install mrtopo

## ONOS INSTALL

sh install-onos-dependencies.sh
sh onos-install.sh

