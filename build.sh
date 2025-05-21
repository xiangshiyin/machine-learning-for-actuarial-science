#!/bin/bash
# poetry export > requirements.txt
uv pip freeze > requirements.txt
docker rmi $(docker images -q mlcourse-image) -f
docker build -t mlcourse-image:latest .