
Step 1 - Cloned the remote github repo to local. Deleted the inherited remote 
         and added my existing remote.

Step 2 - From cli configured the aws account with the provide access keys.

Step 3 - Used python script with 'boto3' to fetch data from DynamoDB table.

Step 4 - Redirected the fetched secret_code from 'stdout' to a new file.

Step 5 - Used Django web framework for development and url routing.

Step 6 - Used JsonResponse class from Django to create a JSON-encoded response.

Step 7 - In Django, used urls.py and view.py in together for url routing.

Step 8 - Used SimpleTestCase class along with 'reverse' and 'resolve' for
         minimal code testing.

Step 9 - Used a Dockerfile with a python base image to containerize the code.

Step 10 - Used docker-compose.yml to build the docker image from the 
          Dockerfile and spin up the container.

Step 11 - Created a .travis.yml file to implement CI process on the Travis CI
          server, whenever a change is pushed on to the Github master branch.

Step 12 - Created a shell script along with the provided verification.sh 
         script as part of the . travis.yml to verify the spinned up container and push the built image to docker hub.
