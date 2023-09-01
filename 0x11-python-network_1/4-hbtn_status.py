#!/usr/bin/python3
"""a Python script that fetches"""
import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)
