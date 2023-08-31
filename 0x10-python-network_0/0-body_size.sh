#!/usr/bin/env bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL="$1"

# Send a request to the URL using curl, follow redirects, and store the response in a temporary file
temp_file=$(mktemp)
curl -sL "$URL" -o "$temp_file"

# Get the size of the response body in bytes and display it
body_size=$(wc -c < "$temp_file")
echo "$body_size"

# Clean up by removing the temporary file
rm "$temp_file"
