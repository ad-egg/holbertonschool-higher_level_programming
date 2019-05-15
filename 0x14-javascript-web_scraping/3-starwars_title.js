#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer
const args = process.argv;
const req = require('request');
let episode = args[2];
let url = 'http://swapi.co/api/films/' + episode
req(url, function (error, response, body) {
  if (error) { console.log(error);
  } else { 
  console.log(JSON.parse(body).title);
  }
} );
