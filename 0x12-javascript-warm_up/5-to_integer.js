#!/usr/bin/node

const arguments = parseInt(process.argv[2]);
if (arguments) {
console.log(`My number: ${arguments}`);
} else {
console.log('Not a number');
}
