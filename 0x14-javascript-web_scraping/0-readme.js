#!/usr/bin/node
# Graham S. Paul ( 0-readme.js)
const fs = require('fs');

const fileName = process.argv[2];
fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
