#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of command line arguments is provided
const filePath = process.argv[2];
  
  fs.readFile(filePath, 'utf8', function(err, data) => {
    if (err) {
      console.error(err);
    } else {
      process.stdout.write(data);
    }
  };
