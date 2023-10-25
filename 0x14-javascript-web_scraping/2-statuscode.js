#!/usr/bin/node

/* Graham S. Paul (2-statuscode.js)
 * Create script that shows the status code of a GET request. */

const request = require('request');

const url = process.argv[2];

request(url, function (error, response) {
  if (!error && response.statusCode) {
    console.log('code:', response.statusCode);
  }
});
