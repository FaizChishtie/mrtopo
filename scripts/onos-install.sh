#!/bin/bash

version="1.9.2"

sudo mkdir /opt
cd /opt

if [ -n "$1" ]
then
    version=$1
fi

echo "Searching for onos version: $version"
sudo wget -c https://repo1.maven.org/maven2/org/onosproject/onos-releases/$version/onos-version.tar.gz
tar xzf onos-$version.tar.gz
mv onos-$version onos

/opt/onos/bin/onos-service start