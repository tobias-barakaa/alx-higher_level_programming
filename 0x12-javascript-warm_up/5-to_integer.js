#!/usr/bin/node

const args = parseInt(process.argv[2]);
if (args) {
console.log(`My number: ${args}`);
} else {
console.log('Not a number');
}
