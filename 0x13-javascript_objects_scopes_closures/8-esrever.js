#!/usr/bin/node
// Graham S. Paul (8-esrever.js)

exports.esrever = function (list) {
  let beg = 0;
  let end = list.length - 1;
  while (beg < end) {
    const tmp = list[beg];
    list[beg] = list[end];
    list[end] = tmp;
    beg++;
    end--;
  }
  return list;
};
