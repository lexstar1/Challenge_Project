#!/bin/bash

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker tag challenge_project_web:latest enochnooli/challenge_project_web:latest
docker push enochnooli/challenge_project_web:latest``
