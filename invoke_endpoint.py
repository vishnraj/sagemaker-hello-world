import boto3
import os

os.environ['AWS_PROFILE'] = 'test-sagemaker-user'

runtime = boto3.client('sagemaker-runtime', region_name='us-east-1')

response = runtime.invoke_endpoint(
    EndpointName='sagemaker-hello-world',
    ContentType='application/json',
    Body='{}'
)

print(response['Body'].read().decode())
