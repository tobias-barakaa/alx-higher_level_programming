#!/usr/bin/node

const arg = process.argv[2];
if (!arg) {
    console.log("No argument");
} else if (arg > 3) {
    console.log(arg);
} else {
   console.log(arg[0]);
}
