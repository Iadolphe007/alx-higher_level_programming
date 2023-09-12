#!/usr/bin/node

const ParentSquare = require('./5-square');

module.exports = class Square extends ParentSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
};
