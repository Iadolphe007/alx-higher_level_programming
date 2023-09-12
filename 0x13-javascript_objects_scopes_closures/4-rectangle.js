#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w >= 1 && h >= 1)) {
      return;
    }
    this.width = w;
    this.height = w;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('x'.repeat(this.width));
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
