#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
const args = process.argv;
const fs = require('fs');
const req = require('request');
let url = args[2];
let filepath = args[3];
req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filepath, body, 'utf8', function (error) {
      if (error) { console.log(error); }
    });
  }
});
