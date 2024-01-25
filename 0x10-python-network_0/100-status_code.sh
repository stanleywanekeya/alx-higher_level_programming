#!/usr/bin/bash
#returns send code
curl -s -o /dev/null -w "%{http_code}" "$1"
