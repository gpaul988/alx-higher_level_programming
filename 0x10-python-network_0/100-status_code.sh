#!/bin/bash
# Graham S. Paul (100-status_code.sh) - Bash scripts thats sends Request
curl -sLIw '%{http_code}' "$1" -o /dev/null
