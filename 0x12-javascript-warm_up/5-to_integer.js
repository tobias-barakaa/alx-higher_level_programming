#!/usr/bin/node

const arguments = process.argv.slice(2)[0];
if (!isNaN(arguments)) {
    console.log('My number:', arguments);
} else {
    const isNumber = parseInt(arguments);
    if (!isNaN(isNumber)) {
        console.log('My number:', isNumber);
    } else {
        console.log('Not a number');
    }
}
