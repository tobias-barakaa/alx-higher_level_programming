#!/usr/bin/node

const args = Number(process.argv[2]);

if (args) {
  for (let i = 0; i < args; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
