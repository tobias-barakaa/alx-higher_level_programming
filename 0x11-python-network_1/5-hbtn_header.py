#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL"""
import requests
import sys

# Check if the correct number of command-line arguments is provided (1 URL)
if len(sys.argv) != 2:
    print("Usage: ./5-hbtn_header.py <URL>")
    sys.exit(1)

# Get the URL from the command-line argument
url = sys.argv[1]

try:
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Raise an exception for HTTP errors (4xx, 5xx)
    response.raise_for_status()

    # Extract the "X-Request-Id" header value from the response
    x_request_id = response.headers.get("X-Request-Id")

    # Print the "X-Request-Id" value
    if x_request_id:
        print(x_request_id)
except requests.exceptions.RequestException as e:
    # Handle any request-related errors and print an error message
    print("Error:", e)
