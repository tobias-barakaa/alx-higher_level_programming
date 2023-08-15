#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.esrever = function (list) {
  const reversed = [];
  
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  
  return reversed;
};
