# LOG8415

Advanced Concepts of Cloud Computing

# Assignment 2

<p>Program that creates and configures an AWS EC2 instance and creates Mysql cluster, upload sakila database to it and do benshmarking>

## Run the program with default credentials

    main.py [-h] [-r] {aws} ...

### optional arguments:

    -h, --help   show this help message and exit
    -r, --reset  reset user's aws account.

## Run the program with manually entered credentials

### aws arguments:

    {aws}
    
    usage: python3.9 main.py aws [-h] -g AWS_REGION_NAME -i AWS_ACCESS_KEY_ID -s AWS_SECRET_ACCESS_KEY -t AWS_SESSION_TOKEN

### optional arguments:

    -h,                         --help                              show this help message and exit
    -g AWS_REGION_NAME,         --region    AWS_REGION_NAME         region name for your AWS account.
    -i AWS_ACCESS_KEY_ID,       --id        AWS_ACCESS_KEY_ID       access key for your AWS account.
    -s AWS_SECRET_ACCESS_KEY,   --secret    AWS_SECRET_ACCESS_KEY   secret key for your AWS account.
    -t AWS_SESSION_TOKEN,       --token     AWS_SESSION_TOKEN       session key for your AWS account.
    -p PROXY_TYPE               --proxy     PROXY_TYPE              The proxy type Direct, Random, Custom
 
## Note:

<p>Experiment results for WordCount and Social Network are saved in <em><strong>time.txt</strong></em> and <em><strong>mutual_friend.txt </strong></em> files respectively..</p>
