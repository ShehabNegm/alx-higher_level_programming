#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const sqr = c;
    const str = sqr.repeat(this.height);
    for (let j = 0; j < this.width; j++) {
      console.log(str);
    }
  }
};
