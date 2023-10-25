#!/usr/bin/node

/* Graham S. Paul (101-starwars_characters.js)
 * Create script that pulls all characters
 * of a Star Wars movie */

const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(apiUrl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printChars(characters, 0);
  }
});

function printChars (characters, i) {
  request(characters[i], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (i + 1 < characters.length) {
        printChars(characters, i + 1);
      }
    }
  });
}
