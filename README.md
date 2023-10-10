The objective of this project is to incorporate URL routing within Django and Dockerize the resultant application. Furthermore, implement Continuous Integration using TravisCI. Upon making changes to the master branch on Github, TravisCI is automatically triggered to integrate the code changes by testing and building the application using the '.travis.yml' file located in the root directory. 

- We use Boto3, an AWS SDK for Python, to extract a string stored in a DynamoDB table in AWS via a Python script. 

- Then, using the Django framework and URL routing, we publish the extracted results at specific paths, such as localhost:5000/path1 and localhost:5000/path2.

- To create a JSON-encoded response, we make use of the JsonResponse class in Django. 

- We verify the results by invoking the web service and retrieving the JSON objects using 'curl' and 'jq.'

- A Docker image of the application is created using the Dockerfile, and then docker-compose.yml is used to build the image and start the service.

- Finally, we implement Continuous Integration through TravisCI. Any changes made to the master on Github triggers TravisCI to integrate the code changes and test and build using the .travis.yml file present in the root.
