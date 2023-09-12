#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w >= 1 && h >= 1)) {
      const newObj = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
