#!/bin/bash
# Graham S. Paul (5-post_params.sh) - Send post Request
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
