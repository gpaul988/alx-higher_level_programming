#!/usr/bin/node
// Graham S. Paul (5-rectangle.js)
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
