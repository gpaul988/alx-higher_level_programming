#!/usr/bin/node
// Graham S. Paul (9-logme.js)

let num = -1;
exports.logMe = function (item) {
  num++;
  console.log(num + ': ' + item);
};
