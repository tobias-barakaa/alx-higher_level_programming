#!/usr/bin/node

const args = Number(process.argv[2]);

if (isNaN(args)) {
     console.log("Missing number of occurrences");
} else {
     for (let i = 0; i < args; i++) {
          console.log("C is fun");
     }
}
