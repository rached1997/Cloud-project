#!/bin/bash

sudo mkdir -p /opt/mysqlcluster/home
cd /opt/mysqlcluster/home
sudo tar xvf /home/ubuntu/mysql-cluster-gpl-7.2.1-linux2.6-x86_64.tar.gz
sudo ln -s mysql-cluster-gpl-7.2.1-linux2.6-x86_64 mysqlc
sudo su <<HERE
echo 'export MYSQLC_HOME=/opt/mysqlcluster/home/mysqlc' > /etc/profile.d/mysqlc.sh
echo 'export PATH=$MYSQLC_HOME/bin:$PATH' >> /etc/profile.d/mysqlc.sh
HERE
source /etc/profile.d/mysqlc.sh
sudo apt-get update
sudo apt-get -y install libncurses5
sudo apt-get install libaio1 libaio-dev


sudo mkdir -p /opt/mysqlcluster/deploy/ndb_data

