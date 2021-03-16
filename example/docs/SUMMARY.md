
Step 1 - Cloned the remote github repo to local. Deleted the inherited remote 
         and added my existing remote.

Step 2 - From cli configured the aws account with the provide access keys.

Step 3 - Used python script with 'boto3' to extract the string from DynamoDB table.

Step 4 - Redirected the extracted secret_code from 'stdout' to a new file.

Step 5 - Used Django web framework for development and url routing.

Step 6 - Created a directory 'my_django_app' and created and activated a virtual environment within the directory

Step 7 - Used JsonResponse class from Django to create a JSON-encoded response.

Step 8 - In Django, used urls.py and views.py together for url routing.

Step 9 - Used SimpleTestCase class along with 'reverse' and 'resolve' for
         minimal code testing.
         
Step 10 - Ran 'python manage.py test' and 'python managa.py runserver' to run tests and start the service.

Step 11 - Stopped the service after invoking the web service and retrieving the JSON objects using 'curl' and 'jq'

Step 12 - Created a .travis.yml file to implement CI process on the Travis CI
          server, whenever a change is pushed on to the Github master branch.
          
Step 13 - Created a shell script along with the provided verification.sh 
         script as part of the .travis.yml file, to push the built image to docker hub after the running web service is invoked

Step 14 - Used a Dockerfile with a python base image to create a Docker image of the application.

Step 15 - Used docker-compose.yml to build the docker image from the 
          Dockerfile and spin up the container.
          
Step 16 - Finally pushed the code to master branch on Github.


