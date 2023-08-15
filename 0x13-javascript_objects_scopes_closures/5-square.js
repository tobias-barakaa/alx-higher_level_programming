#!/usr/bin/node
// class object Rectangle and the constructor with width and height;
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
