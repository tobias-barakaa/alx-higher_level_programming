#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const outputPath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit(1);
  }

  // Write the response body to the specified file (UTF-8 encoded)
  fs.writeFile(outputPath, body, 'utf-8', (error) => {
    if (error) {
      console.log(error);
      process.exit(1);
    }
  });
});
