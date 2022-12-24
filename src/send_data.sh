#!/bin/bash

scp -i ec2_keypair.pem common_setup.sh ubuntu@54.88.113.254:/home/ubuntu
scp -i ec2_keypair.pem mysql-cluster-gpl-7.2.1-linux2.6-x86_64.tar.gz ubuntu@107.21.71.203:/home/ubuntu


scp -i ec2_keypair.pem ndb_mgm_setup.sh ubuntu@54.227.96.203:/home/ubuntu
scp -i ec2_keypair.pem ndb_mgm_setup_2.sh ubuntu@54.227.96.203:/home/ubuntu

ssh -i ec2_keypair.pem ubuntu@23.23.15.243


scp -i ec2_keypair.pem ec2_keypair.pem ubuntu@23.23.15.243:/home/ubuntu

sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h ec2-54-227-96-203.compute-1.amazonaws.com -u w -p


sudo /opt/mysqlcluster/home/mysqlc/bin/mysql_secure_installation

sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h 127.0.0.1 -u root <<BASH_QUERY
SELECT user, host FROM mysql.user;
BASH_QUERY

sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h ip-172-31-29-63 -u test -p <<BASH_QUERY
create database clusterdb;use clusterdb;
create table simples (id int not null primary key) engine=ndb;
insert into simples values (1),(2),(3),(4);
select * from simples;
BASH_QUERY


scp -i ec2_keypair.pem run_sql_command.py ubuntu@54.205.241.255:/home/ubuntu

sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h 127.0.0.1 -u root




bind-address=$1
ndb-connectstring=$1

[mysql_cluster]
ndb-connectstring=$1




