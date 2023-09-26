#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the URL to request from the first command line argument
const url = process.argv[2];

// Make a GET request to the specified URL
request.get(url, (err, response) => {
  if (err) {
    // If there's an error during the request, log the error
    console.log(err);
  } else {
    // If the request is successful, log the HTTP status code from the response
    console.log("code:", response.statusCode);
  }
});
