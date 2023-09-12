#!/usr/bin/node
//Graham S. Paul (5-to_integers.js)
const num = +process.argv[2];

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.floor(num));
}
