#!/bin/bash

option="0"

prompt() {
  echo "MrTopo Script Selector:"
  echo "Option 0 - Run Full VM Install"
  echo "Option 1 - Run Python 3.7.9 Install"
  echo "Option 2 - Run Onos Install"
  echo "Option 3 - Create Virtual Environment (Testing)"
  echo "Option 4 - Remove Virtual Environment (Testing)"
  echo "Type 'q' to quit"
}

select_script () {
  if [ option = "q" ]
  then
    echo "Bye."
    exit 1
  fi
  echo "Selected option $option"
  if [ option = "0" ]
  then
    echo "Full VM Install"
  fi
  if [ option = "1" ]
  then
    echo "Python 3.7.9 Install"
  fi
  if [ option = "2" ]
  then
    echo "Onos Install"
  fi
  if [ option = "3" ]
  then
    echo "Create Virtual Environment"
  fi
  if [ option = "4" ]
  then
    echo "Remove Virtual Environment"
  fi
}

full_vm() {
  sudo sh setup/mininet-vm-setup.sh
}

py_install() {
  sudo sh py-installer/install-py.sh
}

onos_install() {
  sudo sh onos-installer/install-onos-dependencies.sh
  sudo sh onos-install.sh
}

create_test_env() {
  sudo sh test-env/set-test-env.sh
}

remove_test_env() {
  sudo sh test-env/rm-test-env.sh
}

while :
do
  prompt

  read option

  select_script

  echo Success!
done
