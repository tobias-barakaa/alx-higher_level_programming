#!/usr/bin/node
// empty class object Rectangle and the constructor;
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h; 
    }
  }
}

module.exports = Rectangle;
