import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Define the name of the bucket
bucket_name = 'webdatabase'

# Define the name of the file to upload
file_name = 'image.jpg'

# Define the name to give to the object in the bucket
object_name = 'images/image.jpg'

# Upload the file to the bucket
s3.upload_file(file_name, bucket_name, object_name)

print(f'File {file_name} has been uploaded to {bucket_name} as {object_name}.')

