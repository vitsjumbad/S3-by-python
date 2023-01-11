import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Define the name of the new bucket
bucket_name = 'webdatabase'

# Create the new bucket
s3.create_bucket(Bucket=bucket_name)

# Wait for the bucket to be created
s3.get_waiter('bucket_exists').wait(Bucket=bucket_name)

# Print a message to confirm that the bucket has been created
print(f'Bucket {bucket_name} has been created.')

