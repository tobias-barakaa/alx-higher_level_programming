#!/usr/bin/node

const n = parseInt(process.argv[2]);

function factorial (n) {
  if (Number.isNaN(n) || n === 0) {
    return (1);
  }
  if (n < 0) {
    return (-1);
  }
  return (n * factorial(n - 1));
}

const fact = factorial(n);
console.log(fact);
