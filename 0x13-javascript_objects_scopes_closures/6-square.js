#!/usr/bin/node

const extSqr = require('./5-square');

class Square extends extSqr {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; ++i) {
      let str = '';
      for (let j = 0; j < this.width; ++j) {
        str += c;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
