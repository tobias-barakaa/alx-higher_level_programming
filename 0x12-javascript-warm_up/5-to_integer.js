#!/usr/bin/node

const numVar = parseInt(process.argv[2]);
if (numVar) {
  console.log(`My number: ${numVar}`);
} else {
  console.log('Not a number');
}
