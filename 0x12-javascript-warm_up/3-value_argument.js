#!/usr/bin/node

const argument = process.argv[2];

if (argument) {
  console.log(argument);
} else {
  console.log('No argument');
}
