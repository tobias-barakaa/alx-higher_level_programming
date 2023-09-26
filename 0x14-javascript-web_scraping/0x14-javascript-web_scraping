#!/usr/bin/node

/**
 * Read and print the content of a file.
 *
 * Usage: ./0-readme.js <file_path>
 * Example: ./0-readme.js cisfun
 */

const fs = require('fs');

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the content of the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
