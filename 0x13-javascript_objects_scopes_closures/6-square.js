#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const sqr = 'X';
    const str = sqr.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(str);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

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
