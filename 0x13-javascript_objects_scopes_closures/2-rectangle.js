#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w >= 1 && h >= 1)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
};
