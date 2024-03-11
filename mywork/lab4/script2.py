#!/usr/bin/env python3

import boto3
import requests

s3 = boto3.client('s3', region_name="us-east-1")

# Getting Image: https://blog.finxter.com/5-easy-ways-to-download-an-image-from-a-url-in-python/

url = 'https://wanderlustbee.com/wp-content/uploads/2023/09/IMG_8800-scaled-e1699088963675-1440x1459.jpeg'
response = requests.get(url)

if response.status_code == 200:
	with open('rome.jpg', 'wb') as f:
		f.write(response.content)

	#Image has been saved as 'rome.jpg', next step add to s3
	bucket = 'ds2002-ebo4dq'
	local_file = 'rome.jpg'

	#https://stackoverflow.com/questions/14150854/aws-s3-display-file-inline-instead-of-force-download

	resp = s3.put_object(
		Body = response.content,
		Bucket = bucket,
		Key = local_file,
		ContentType = 'image/jpeg'
	)

	#Presign the file
	response = s3.generate_presigned_url(
		'get_object',
		Params = {'Bucket' : bucket, 'Key': local_file},
		ExpiresIn = 604800
	)
	print("The presigned url is", response)

else:
	print("Error getting image")




#Final Presigned URL:
# https://ds2002-ebo4dq.s3.amazonaws.com/rome.jpg?AWSAccessKeyId=ASIAZQ3DUDCE7YCRNHOK&Signature=%2FiMUbW8rY%2BKe76eMHgZi6ux6yQw%3D&x-amz-security-token=FwoGZXIvYXdzEDoaDDOh%2By5uDfZObPyezSLEAW%2BzBPoXAQpKnzwDfEw5XYheicMTAdIdHkLRlpeaDj2qgggtzpQFmni3HWGK8PalOi1bZr31B%2FTWNm1ZqvAgrQTeIY9w9bGPqjcxqrXtw4lByc9Yaufx6FADjUqw43ZZ%2FpkgcSexEZjw4iq6Dof884%2Boa4G31joLnSkArQjwZaWC%2BLQY%2Fh9YFNrkZOTNm%2FMQjXUl9yjjjf%2BixtMSoza3wJ8qWxH5rWBoH39owhm%2FXut27tiw0ns0cP9GYEqXk20AIS5OVGIo3fK8rwYyLR6MAbNxU5%2BZTvobyWtJVGQJn4TISoQTED2AuzsH4%2FVUWAczTxta0H%2BZaVT5CQ%3D%3D&Expires=1710789916
