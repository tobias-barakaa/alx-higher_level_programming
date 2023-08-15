#!/usr/bin/node
// function that returns the number of occurrences in a list
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};

