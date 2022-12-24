#!/bin/bash

sudo /opt/mysqlcluster/home/mysqlc/bin/ndb_mgm -e show
sleep 2m
sudo /opt/mysqlcluster/home/mysqlc/bin/ndb_mgm -e show
sudo /opt/mysqlcluster/home/mysqlc/bin/mysqld --defaults-file=/opt/mysqlcluster/deploy/conf/my.cnf --user=root &
sleep 3m
sudo /opt/mysqlcluster/home/mysqlc/bin/ndb_mgm -e show

sudo /opt/mysqlcluster/home/mysqlc/bin/mysql <<BASH_QUERY
CREATE USER 'test'@'%' IDENTIFIED BY 'test';
GRANT ALL PRIVILEGES ON * . * TO 'test'@'%' IDENTIFIED BY 'test';
BASH_QUERY

sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h $1 -u test -ptest <<BASH_QUERY
create database clusterdb;use clusterdb;
create table simples (id int not null primary key) engine=ndb;
insert into simples values (1),(2),(3),(4);
select * from simples;
BASH_QUERY



