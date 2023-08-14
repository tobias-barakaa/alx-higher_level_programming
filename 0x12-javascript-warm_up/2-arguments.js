#!/usr/bin/node

const arguments = process.argv;
if (arguments.length === 2) {
  console.log('No arguments');
} else if (arguments.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
