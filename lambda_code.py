import json  # Import the JSON module to handle JSON data
import boto3  # Import the Boto3 library to interact with AWS services

def lambda_handler(event, context):
    # Create an SSM client to interact with the AWS Systems Manager
    client = boto3.client("ssm")
    
    # Define the command to run a Docker container using CentOS 7 in Detached mode
    cmd = {'commands': ['docker run -dit centos:7']}
    
    # Send the command to the specified EC2 instance using the AWS-RunShellScript document
    client.send_command(DocumentName="AWS-RunShellScript", InstanceIds=['i-083f2aca2b9664d91'], Parameters=cmd)
    
    # Return a successful response with a message
    return {
        'statusCode': 200,
        'body': json.dumps('+1 Container launched')
    }
