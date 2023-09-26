#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require("request");

// Get the URL to make a request to from the command-line arguments
const url = process.argv[2];

// Use the 'request' module to make an HTTP request to the provided URL
request(url, (err, response) => {
  if (err) {
    // If there is an error, log the error message
    console.error(err.message);
  } else {
    // If the request is successful, log the HTTP status code
    console.log(`HTTP Status Code: ${response.statusCode}`);
  }
});
