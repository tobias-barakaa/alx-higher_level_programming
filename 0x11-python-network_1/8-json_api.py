#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

# If no argument is given, set q=""
if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

# Create a dictionary with the letter parameter
data = {'q': q}

try:
    # Send a POST request to the specified URL with the letter parameter
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    # Try to parse the response JSON
    user_info = response.json()

    # Check if the JSON response is properly formatted and not empty
    if user_info:
        print("[{}] {}".format(user_info.get('id'), user_info.get('name')))
    else:
        print("No result")
except ValueError:
    # Handle JSON parsing errors
    print("Not a valid JSON")
except requests.exceptions.RequestException as e:
    # Handle any request-related errors and print an error message
    print("Error:", e)
