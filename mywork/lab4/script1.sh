#!/bin/bash

URL="https://wanderlustpulse.com/wp-content/uploads/2023/04/Guide-Amalfi-Coast-Map.jpg"

curl $URL > image.jpg

aws s3 cp image.jpg s3://ds2002-ebo4dq/

aws s3 presign --expires-in 604800 s3://ds2002-ebo4dq/image.jpg

#Link Generated
# Here
