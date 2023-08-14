#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  const element = a + b;
  return (element);
}

console.log(add(a, b));
