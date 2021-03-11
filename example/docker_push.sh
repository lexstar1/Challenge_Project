#!/bin/bash

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker tag my_django_app_web enochnooli/my_django_app_web
docker push enochnooli/my_django_app_web