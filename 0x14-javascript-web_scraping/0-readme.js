#!/usr/bin/node

/**
 * Read and print the content of a file.
 *
 * Usage: ./0-readme.js <file_path>
 * Example: ./0-readme.js cisfun
 */

const fs = require('fs');

// Check if the correct number of command line arguments is provided
if (process.argv.length < 3) {
  console.log("Usage: ./0-readme.js <file_path>");
} else {
  const filePath = process.argv[2];
  
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      process.stdout.write(data);
    }
  });
}
