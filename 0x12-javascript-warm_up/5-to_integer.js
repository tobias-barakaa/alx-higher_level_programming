#!/usr/bin/node

const arguments = process.argv[2];
if (!isNaN(arguments)) {
    console.log('My number:', arguments);
} else {
        console.log('Not a number');
}
