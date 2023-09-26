#!/usr/bin/node

// Include the 'fs' module to work with the file system
const fs = require('fs');

// Get the file path and content from command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Use fs.writeFile to write the content to the specified file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // If there is an error, log it to the console
    console.log(err);
  }
});
