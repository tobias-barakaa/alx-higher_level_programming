#!/usr/bin/node
// a function that converts to binary or base 10
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
