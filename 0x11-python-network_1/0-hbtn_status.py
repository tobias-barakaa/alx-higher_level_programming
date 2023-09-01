#!/usr/bin/python3
""" Python script that fetches"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        # Read the response body
        response_data = response.read()

        # Display the response information
        print("Body response:")
        print(f"    - type: {type(response_data)}")
        print(f"    - content: {response_data}")
        print(f"    - utf8 content: {response_data.decode('utf-8')}")
