#!/usr/bin/python3
"""
a Python script that takes in a URL and an email,
sends a POST
"""
import urllib.request
import urllib.parse
import sys

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

# Get the URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Encode the email parameter to be sent in the POST request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

# Create a POST request with the email parameter
req = urllib.request.Request(url, data=data, method='POST')

try:
    # Send the POST request and open the response
    with urllib.request.urlopen(req) as response:
        # Read and decode the response body in utf-8
        body = response.read().decode('utf-8')
        # Display the decoded response body
        print(body)
except urllib.error.URLError as e:
    # Handle any URL-related errors
    print("Error:", e)
