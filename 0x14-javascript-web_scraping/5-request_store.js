#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: node 5-request_store.js <URL> <outputFilePath>');
  process.exit(1);
}

const url = process.argv[2];
const outputPath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.log('HTTP Request Failed with Status Code:', response.statusCode);
    process.exit(1);
  }

  // Write the response body to the specified file (UTF-8 encoded)
  fs.writeFile(outputPath, body, 'utf-8', (error) => {
    if (error) {
      console.log('Error writing to file:', writeError);
      process.exit(1);
    }
    console.log('File saved successfully:', outputPath);
  });
});
