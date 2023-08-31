#!/bin/bash

# Get the URL from the user
url=$1

# Use curl to get the response body size
body_size=$(curl -s -I "$url" | grep -Po 'Content-Length:\s*([0-9]+)')

# Print the body size
echo "Body size: ${body_size} bytes"
