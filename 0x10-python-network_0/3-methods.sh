#!/bin/bash 
# Graham S. Paul (3-methods.sh) - Pull options in HEAD
curl -sI "$1" | grep "Allow:" | cut -d" " -f2-
