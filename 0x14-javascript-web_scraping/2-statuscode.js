#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (err, response) => {
  if (err) {
    // Log an informative error message
    console.log(err.message);
  } else {
    console.log("code:", response.statusCode);
  }
});
