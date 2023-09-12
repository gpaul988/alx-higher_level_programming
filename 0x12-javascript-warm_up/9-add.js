#!/usr/bin/node
// Graham S. Paul (9-add.js)
function add (a, b) {
  console.log(a + b);
}

const a = +process.argv[2];
const b = +process.argv[3];

add(a, b);
