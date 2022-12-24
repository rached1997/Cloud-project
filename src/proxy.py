import pymysql.cursors
import argparse
import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import random
from pythonping import ping


def run_direct(pub_master_ip_address):
    # Connect to the database
    connection = pymysql.connect(host=pub_master_ip_address, user='test', password='test', database='sakila', cursorclass=pymysql.cursors.DictCursor)


    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT COUNT(*) FROM `actor`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `actor` VALUES (10000000, 'Fred', 'Simpson', '2015-06-20 14:00:00');"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT COUNT(*) FROM `actor`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)


def run_random(pub_master_ip_address, pub_slaves_ip_addresses):
    pub_slaves_ip_address = pub_slaves_ip_addresses[random.randint(0, 3)]
    mypkey = paramiko.RSAKey.from_private_key_file('/home/ubuntu/ec2_keypair.pem')
    # if you want to use ssh password use - ssh_password='your ssh password', bellow
    sql_hostname = pub_master_ip_address  # IP public du master
    sql_username = 'test'
    sql_password = 'test'
    sql_main_database = 'sakila'
    sql_port = 3306
    ssh_host = pub_slaves_ip_address  # IP public du slave
    ssh_user = 'ubuntu'
    ssh_port = 22
    with SSHTunnelForwarder((ssh_host, ssh_port), ssh_username=ssh_user, ssh_pkey=mypkey,
                            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(host='127.0.0.1', user=sql_username, passwd=sql_password, db=sql_main_database,
                               port=tunnel.local_bind_port)
        query = "SELECT COUNT(*) FROM `actor`"
        data = pd.read_sql_query(query, conn)
        conn.close()
    print(data)


def custom(ip_addresses):
    responses = {}

    for node in ip_addresses:
        response = ping(node)
        responses[node]=response.rtt_avg

    best_node = min(responses, key=responses.get)
    best_node= str(best_node)

    return(best_node)


def run_custom(pub_master_ip_address, pub_slaves_ip_addresses):
    best_node = custom(pub_slaves_ip_addresses + [pub_master_ip_address])
    if best_node == pub_master_ip_address:
        connection = pymysql.connect(host=best_node, user='test', password='test', database='sakila',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT COUNT(*) FROM `actor`"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
    else:
        mypkey = paramiko.RSAKey.from_private_key_file('/home/ubuntu/ec2_keypair.pem')
        # if you want to use ssh password use - ssh_password='your ssh password', bellow
        sql_hostname = pub_master_ip_address  # IP public du master
        sql_username = 'test'
        sql_password = 'test'
        sql_main_database = 'sakila'
        sql_port = 3306
        ssh_host = best_node  # IP public du slave
        ssh_user = 'ubuntu'
        ssh_port = 22
        with SSHTunnelForwarder((ssh_host, ssh_port), ssh_username=ssh_user, ssh_pkey=mypkey,
                                remote_bind_address=(sql_hostname, sql_port)) as tunnel:
            conn = pymysql.connect(host='127.0.0.1', user=sql_username, passwd=sql_password, db=sql_main_database,
                                   port=tunnel.local_bind_port)
            query = "SELECT COUNT(*) FROM `actor`"
            data = pd.read_sql_query(query, conn)
            conn.close()
        print(data)


def main():
    parser = argparse.ArgumentParser(
        description=('description')
    )

    parser.add_argument('-m', help='Master node public IP address.', est='MIP', required=True)
    parser.add_argument('-dn1', help='data node 1 public IP address.', dest='N1_IP', required=True)
    parser.add_argument('-dn2', help='data node 2 public IP address.',  dest='N2_IP', required=True)
    parser.add_argument('-dn3', help='data node 3 public IP address.', dest='N3_IP', required=True)
    parser.add_argument('-p', help='The proxy type : Direct, Random, Custom',  dest='MODE', required=True)

    args = parser.parse_args()

    if args.MODE == 'direct':
        run_direct(args.MIP)
    elif args.MODE == 'random':
        run_random(args.MIP, [args.N1_IP, args.N2_IP, args.N3_IP])
    else:
        run_custom(args.MIP, [args.N1_IP, args.N2_IP, args.N3_IP])

if __name__ == '__main__':
    main()


