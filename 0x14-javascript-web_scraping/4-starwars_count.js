#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present
const args = process.argv;
const req = require('request');
let url = args[2];
req(url, function (error, response, body) {
  if (error) { console.log(error);
  } else {
    let films = JSON.parse(body);
    let num = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('/18/')) { num++; }
      }
    }
    console.log(num);
  }
});
