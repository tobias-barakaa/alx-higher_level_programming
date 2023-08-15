#!/usr/bin/node
// convert to base
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};

