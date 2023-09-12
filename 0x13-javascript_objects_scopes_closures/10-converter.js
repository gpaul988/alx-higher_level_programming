#!/usr/bin/node
// Graham S. Paul (10-converter.js)

exports.converter = function (base) {
  function convert (n) {
    return n.toString(base);
  }
  return convert;
};
