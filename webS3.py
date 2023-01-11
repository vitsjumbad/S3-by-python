import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Create a new S3 bucket for the website
bucket_name = 'example-static-website'
s3.create_bucket(Bucket=bucket_name)

# Wait for the bucket to be created
s3.get_waiter('bucket_exists').wait(Bucket=bucket_name)

# Set the policy for the bucket to allow public read access
policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
}
s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))

# Enable website hosting for the bucket
s3.put_bucket_website(
    Bucket=bucket_name, 
    WebsiteConfiguration={
        'ErrorDocument': {
            'Key': 'error.html'
        },
        'IndexDocument': {
            'Suffix': 'index.html'
        }
    }
)

#Upload your index.html and error.html in the same bucket
s3.upload_file('index.html', bucket_name, 'index.html')
s3.upload_file('error.html', bucket_name, 'error.html')

# Print the website endpoint
response = s3.get_bucket_website(Bucket=bucket_name)
website_endpoint = response['WebsiteEndpoint']
print(f'Static website endpoint: {website_endpoint}')

