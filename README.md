This is a simple project to implement 'url routing' in Django and to Dockerize the application. Continuous Integration is implemented using TravisCI. Any change made to the master on Github, triggers TravisCI to integrate the code changes and be tested and built using the '.travis.yml' file present in the root

1)Firstly we extract a string stored in DynamoDB table in AWS via a python script using 'boto3' a AWS SDK for Python (Boto3) to create, configure, and manage AWS services

2)Then via 'url routing' using Django framework, we publish the extracted results at specific paths. Eg: localhost:5000/path1,localhost:5000/path2 etc.,

3)We use the 'JsonResponse' class in Django to create a JSON-encoded response

4)We use 'curl' and 'jq' to verify the same by invoking the web service and retrieving the JSON objects

5)A Docker image of the application is created via the Dockerfile. 'docker-compose.yml' is used to build the image and start the the service 

6)Continuous Integration is implemented using TravisCI. Any change made to the master on Github, triggers TravisCI to integrate the code changes and be tested and built using the '.travis.yml' file present in the root
