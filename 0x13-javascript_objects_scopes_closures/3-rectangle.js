#!/usr/bin/node
// class object Rectangle and the constructor with width and height;
class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }
  
  print () {
    for (let i = 0; i < this.width; i++) {
      let row = "";
      for (let j = 0; j < this.height; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
