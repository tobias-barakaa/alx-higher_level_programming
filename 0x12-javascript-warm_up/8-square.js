#!/usr/bin/node

const args = parseInt(process.argv[2]);

if (!isNaN(args)) {
  const row = 'X'.repeat(args);
  for (let i = 0; i < args; i++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
