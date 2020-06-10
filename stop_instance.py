import boto3

region = 'region-identification'#Ex: us-east-2

instances = ['id-intance']#Ex: i-1c2e44ac00f0e5d85

def lambda_handler(event, context):
    
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)