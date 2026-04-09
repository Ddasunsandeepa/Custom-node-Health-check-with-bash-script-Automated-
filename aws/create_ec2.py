import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

instances = ec2.create_instances(
    ImageId='ami-0ec10929233384c7f',
    InstanceType='t3.micro',
    KeyName='my-cloud',
    SecurityGroupIds=['sg-08d001ac5518b6750'],
    SubnetId='subnet-0162ef878c072c011',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyUbuntuServer'}
            ]
        }
    ]
)

instance = instances[0]

print("Waiting for instance to run...")
instance.wait_until_running()

instance.reload()

print(f"Instance ID: {instance.id}")
print(f"Public IP: {instance.public_ip_address}")