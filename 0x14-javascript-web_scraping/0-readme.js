#!/usr/bin/node

/* Graham S. Paul (0-readme.js)
 * Script that reads and pull the content of a file
 */

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (error, content) => {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
