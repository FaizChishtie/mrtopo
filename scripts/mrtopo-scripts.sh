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
  if [ "$1" = "q" ]
  then
    echo "Bye."
    exit 1
  fi
  echo "Selected option $option"
  if [ "$1" = "0" ]
  then
    echo "Full VM Install"
    return 1
  fi
  if [ "$1" = "1" ]
  then
    echo "Python 3.7.9 Install"
    return 1
  fi
  if [ "$1" = "2" ]
  then
    echo "Onos Install"
    return 1
  fi
  if [ "$1" = "3" ]
  then
    echo "Create Virtual Environment"
    return 1
  fi
  if [ "$1" = "4" ]
  then
    echo "Remove Virtual Environment"
    return 1
  fi
  return 0
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

  status="$(select_script "$option")"

  if [ "$status" != "0" ]
  then
    echo Success!
  else
    echo Something went wrong! Please try again. 
  fi
done
