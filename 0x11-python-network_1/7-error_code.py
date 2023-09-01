#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the
URL and displays the body of the response
"""
import requests
import sys

# Get the URL from command-line arguments
url = sys.argv[1]

try:
    # Send a GET request to the specified URL
    response = requests.get(url)
    # Display the response body
    print(response.text)

    # Check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
except requests.exceptions.RequestException as e:
    # Handle any request-related errors and print an error message
    print("Error:", e)
