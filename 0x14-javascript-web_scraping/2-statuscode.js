#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require("request");

// Get the URL to make a request to from the command-line arguments
const url = process.argv[2];

// Use the 'request' module to make an HTTP request to the provided URL
request(url, (err, response) => {
  console.log("Code :", response.statusCode);
}
