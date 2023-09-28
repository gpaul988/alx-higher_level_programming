#!/bin/bash
# Graham S. Paul (101-post_json.sh) - Bash scripts that send JSOn Post Request
curl -sLX POST -H 'Content-Type: application/json' -d @"$2" "$1"
