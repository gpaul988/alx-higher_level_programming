#!/usr/bin/node

/* Graham S. Paul (100-starwars_characters.js)
 * Create script that pulls all characters
 * of a Star Wars movie */

const req = require('request');
const uri = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(uri, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      req(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
