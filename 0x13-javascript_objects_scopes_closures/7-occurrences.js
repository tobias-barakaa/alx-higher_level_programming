#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let j = 0; j < list.length; j++) {
    if (list[j] === searchElement) {
      count++;
    }
  }
  return count;
};
