Problem 1:
Took a while to properly understand the requirements and visualize the workflow.
Started working on one requirement at a time made the desired outcome clearer.

Problem 2:
Was unable to obtain the AWS region needed to configure aws account.
Made use of the available 'us' regions to check for no error response
to figure out the region.

Problem 3:
Given the requirements, using 'Python' seemed the best option. But had to familiarize myself with 'boto3', a python SDK for AWS

Problem 4:
Was not very sure of the DynamoDB table schema
Researched and implemented the provided table values as part of the Script

Problem 5:
Django framework felt a bit complicated but referring to different use-case scenarios, helped to figure out the requirements for the given project. Although using 'Flask' would've been simpler and better. 

Problem 6:
Initially used 'CMD' as part of the Dockerfile which wasn't the right approach, given the requirement.
Instead used docker-compose.yml to build the image from Dockerfile and specify the 'command' to run within the container to start the application and be made available on the specified port configuration.

Problem 7:
After the container was up, the verfication.sh script was run but returned no data.
This was because of the 'jq' JSON-processor. Implementing the 'JsonResponse' class from Django fixed the issue

Problem 8:
In the Travis CI build, again the verification.sh script did not return any data.
This was because I mentioned the url paths as health/ and secret/ instead of 
/health and /secret in the urls.py file. Changing the paths fixed the issue.

Problem 9: 
In the Travis CI build the docker_push.sh script failed to execute as the wrong image name was given. Including 'docker images' command right after the build as part of the .travis.yml file helped figure the correct image name which fixed the issue.