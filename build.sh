#!/bin/bash

docker rmi $(docker images -q mlcourse-image) -f
docker build -t mlcourse-image:latest .