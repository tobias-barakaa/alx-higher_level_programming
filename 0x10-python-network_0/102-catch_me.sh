#!/bin/bash

# Send a PUT request with a custom User-Agent header
curl -sX PUT -H "User-Agent: I am a curl request" 0.0.0.0:5000/catch_me -d "user_id=98" -L
