#!/usr/bin/node

const arguments = process.argv[2];
if (arguments) {
    console.log(`My number: ${arguments}`);
} else {
    console.log('Not a number');
}
