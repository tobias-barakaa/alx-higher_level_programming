#!/bin/bash
# a Bash script that sends a DELETE request to the URL passed as the first argument
curl -s -X DELETE "$1"
