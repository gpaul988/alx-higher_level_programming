#!/usr/bin/node
// Graham S. Paul (6-square.js)
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.width; col += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
