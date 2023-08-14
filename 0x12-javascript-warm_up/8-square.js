#!/usr/bin/node

const args = parseInt(process.argv[2]);

if (!isNaN(args)) {
  for (let i = 0; i < args; i++) {
     let row = "";
     for (let j = 0; j < args; j++) {
          row += "x";
      }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
