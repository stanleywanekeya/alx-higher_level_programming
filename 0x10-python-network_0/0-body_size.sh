#!/bin/bash
#sends a request
curl -s "$1" | wc -c
