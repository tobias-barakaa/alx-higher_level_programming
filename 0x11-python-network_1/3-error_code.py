#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL"""
import urllib.request
import urllib.error
import sys

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 2:
    print("Usage: ./3-error_code.py <URL>")
    sys.exit(1)

# Get the URL from the command-line argument
url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Read and decode the response body in utf-8
        body = response.read().decode('utf-8')
        # Display the decoded response body
        print(body)
except urllib.error.HTTPError as e:
    # Handle HTTP errors by printing the error code
    print("Error code:", e.code)
