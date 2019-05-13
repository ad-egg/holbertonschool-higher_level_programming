#!/usr/bin/node
// a class Square that defines a square and inherits from Rectangle class of
// 4-rectangle.js
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) { super(size, size); }
  charPrint (c) {
    if (c == null) { c = 'X'; }
    for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
  }
};
