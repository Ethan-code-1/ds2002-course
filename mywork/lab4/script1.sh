#!/bin/bash

URL="https://wanderlustpulse.com/wp-content/uploads/2023/04/Guide-Amalfi-Coast-Map.jpg"

curl $URL > image.jpg

aws s3 cp image.jpg s3://ds2002-ebo4dq/

aws s3 presign --expires-in 604800 s3://ds2002-ebo4dq/image.jpg

#Link Generated
# https://ds2002-ebo4dq.s3.us-east-1.amazonaws.com/image.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAZQ3DUDCE7YCRNHOK%2F20240311%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240311T172322Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEDoaDDOh%2By5uDfZObPyezSLEAW%2BzBPoXAQpKnzwDfEw5XYheicMTAdIdHkLRlpeaDj2qgggtzpQFmni3HWGK8PalOi1bZr31B%2FTWNm1ZqvAgrQTeIY9w9bGPqjcxqrXtw4lByc9Yaufx6FADjUqw43ZZ%2FpkgcSexEZjw4iq6Dof884%2Boa4G31joLnSkArQjwZaWC%2BLQY%2Fh9YFNrkZOTNm%2FMQjXUl9yjjjf%2BixtMSoza3wJ8qWxH5rWBoH39owhm%2FXut27tiw0ns0cP9GYEqXk20AIS5OVGIo3fK8rwYyLR6MAbNxU5%2BZTvobyWtJVGQJn4TISoQTED2AuzsH4%2FVUWAczTxta0H%2BZaVT5CQ%3D%3D&X-Amz-Signature=a422247cd3a6ca8c6028735563328bf429ebc32a9f746f8bef7929a3746683e8
