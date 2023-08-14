#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

if(args) {
     for (let i = 0; i < args.length; i++) {
     console.log("C is fun");
     } 
} else {
     console.log("Missing number of occurrences");
}
