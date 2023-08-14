#!/usr/bin/node

const arguments = process.argv.slice(2); // Get command-line arguments

if (arguments.length === 0) {
  console.log("No arguments");
} else if (arguments.length === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
