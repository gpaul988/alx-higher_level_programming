#!/usr/bin/node

/* Graham S. Paul (3-starwars_title.js)
 * Create script that pulls the title of
 * a Star Wars movie where the episode */

const req = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(starWarsUri, function (error, res, body) {
  console.log(error || JSON.parse(body).title);
});
