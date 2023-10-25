#!/usr/bin/node
/* Graham S. Paul (5-request_store.js)
 * Create script that gets the contents of a webpage
 * and stores it in a file.*/

const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
const apiUrl = args[0];
const file = args[1];
request(apiUrl).pipe(fs.createWriteStream(file));
