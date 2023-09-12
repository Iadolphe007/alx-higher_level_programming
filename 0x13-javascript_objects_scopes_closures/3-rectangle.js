#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w >= 1 && h >= 1)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let size = ' ';
      for (let j = 0; j < this.width; j++) {
        size += 'X';
      }
      console.log(size);
    }
  }
};
