#!/usr/bin/node
//  imports a dictionary of occurrences by user id and computes
const data = require('./101-data');
const originalDict = data.dict;

const invertedDict = {};

for (const userId in originalDict) {
  const occurrences = originalDict[userId];

  if (occurrences in invertedDict) {
    invertedDict[occurrences].push(userId);
  } else {
    invertedDict[occurrences] = [userId];
  }
}

console.log(invertedDict);
