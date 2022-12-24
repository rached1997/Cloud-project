EC2_CONFIG = {
    'Common': {
        'ServiceName': 'ec2',
        # 'ImageId': 'ami-08c40ec9ead489470',  # Ubuntu, 22.04 LTS, 64-bit (x86)
        'ImageId': 'ami-061dbd1209944525c',  # Ubuntu, 18.04 LTS, 64-bit (x86)
        'KeyPairName': 'log8415_lab1_kp',
        'SecurityGroups': ['log8415_lab1_sg'],
        'InstanceCount': 1,
        'InstanceProfileName': 'LabInstanceProfile',  # We'll use this default role since we can't create a new one.
        'MetadataOptions': {
            'InstanceMetadataTags': 'enabled'
        }
    },
    'Cluster1': {
        'InstanceType': 't2.micro',
        'AvailabilityZone': 'us-east-1a',
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Cluster', 'Value': '1', },
                    {'Key': 'Instance', 'Value': '', }  # Instance tag value is given when creating the instance
                ]
            }
        ]
    },
    'Cluster2': {
        'InstanceType': 't2.large',
        'AvailabilityZone': 'us-east-1a',
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Cluster', 'Value': '2', },
                    {'Key': 'Instance', 'Value': '', }  # Instance tag value is given when creating the instance
                ]
            }
        ]
    }
}

SSH_CONFIG_STAND_ALONE = {
    'EC2UserName': 'ubuntu',
    'KeyPairFile': 'ec2_keypair.pem',
    'FilesToUpload': [
        './stand_alone.sh',
    ],
    'RemoteDirectory': '/home/ubuntu/',
    'ScriptToExecute': '/home/ubuntu/stand_alone.sh'
}

SSH_CONFIG_NODE_MANAGER = {
    'EC2UserName': 'ubuntu',
    'KeyPairFile': 'ec2_keypair.pem',
    'FilesToUpload': [
        'mysql-cluster-gpl-7.2.1-linux2.6-x86_64.tar.gz',
        'ndb_mgm_setup.sh',
    ],
    'RemoteDirectory': '/home/ubuntu/',
    'ScriptToExecute': '/home/ubuntu/ndb_mgm_setup.sh'
}

SSH_CONFIG_DATA_NODE = {
    'EC2UserName': 'ubuntu',
    'KeyPairFile': 'ec2_keypair.pem',
    'FilesToUpload': [
        'mysql-cluster-gpl-7.2.1-linux2.6-x86_64.tar.gz',
        'data_node_setup.sh',
    ],
    'RemoteDirectory': '/home/ubuntu/',
    'ScriptToExecute': '/home/ubuntu/data_node_setup.sh'
}

SSH_CONFIG_SQL_Node = {
    'EC2UserName': 'ubuntu',
    'KeyPairFile': 'ec2_keypair.pem',
    'FilesToUpload': [
        'sql_node_setup.sh',
        'sql_node_create_db.sh',
    ],
    'RemoteDirectory': '/home/ubuntu/',
    'ScriptToExecute': ['/home/ubuntu/sql_node_setup.sh', '/home/ubuntu/sql_node_create_db.sh']
}

SSH_CONFIG_PROXY = {
    'EC2UserName': 'ubuntu',
    'KeyPairFile': 'ec2_keypair.pem',
    'FilesToUpload': [
        'ec2_keypair.pem',
        'proxy.py',
        'run_proxy.sh',
    ],
    'RemoteDirectory': '/home/ubuntu/',
    'ScriptToExecute': '/home/ubuntu/run_proxy.sh'
}
