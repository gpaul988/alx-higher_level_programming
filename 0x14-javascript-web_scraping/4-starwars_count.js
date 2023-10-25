#!/usr/bin/node

/* Graham S. Paul (4-starwars_count.js)
 * Create script that pulls the number of movies
 * where the character "Wedge Antilles" is present. */

const req = require('request');

req(process.argv[2], function (error, res, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((i, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? i + 1
        : i;
    }, 0));
  }
});
