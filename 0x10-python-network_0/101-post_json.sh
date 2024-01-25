#!/usr/bin/bash
#sends a json as post request
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
