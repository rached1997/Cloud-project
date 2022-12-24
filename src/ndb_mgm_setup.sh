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

sudo mkdir -p /opt/mysqlcluster/deploy
cd /opt/mysqlcluster/deploy
sudo mkdir conf
sudo mkdir mysqld_data
sudo mkdir ndb_data
cd conf

sudo su <<HERE
echo "[mysqld]
ndbcluster
datadir=/opt/mysqlcluster/deploy/mysqld_data
basedir=/opt/mysqlcluster/home/mysqlc
port=3306
bind-address=0.0.0.0" >> my.cnf

echo "[ndb_mgmd]
hostname=$1
datadir=/opt/mysqlcluster/deploy/ndb_data
nodeid=1
[ndbd default]
noofreplicas=3
datadir=/opt/mysqlcluster/deploy/ndb_data
[ndbd]
hostname=$2
nodeid=3
[ndbd]
hostname=$3
nodeid=4
[ndbd]
hostname=$4
nodeid=5
[mysqld]
nodeid=50">> config.ini
HERE

cd /opt/mysqlcluster/home/mysqlc
sudo scripts/mysql_install_db --no-defaults --datadir=/opt/mysqlcluster/deploy/mysqld_data
