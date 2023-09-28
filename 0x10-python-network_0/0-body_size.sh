#!/bin/bash
# Graham S. Paul (0-body_size.sh) - Pull curl detail size
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
