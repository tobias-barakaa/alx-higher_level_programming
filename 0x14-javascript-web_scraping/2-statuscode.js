#!/usr/bin/node

const request = require('request');

// Get the URL to request from the first command line argument
const url = process.argv[2];

// Make a GET request to the URL
request.get(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
  console.log("code: ", response.statusCode);
  }
}
