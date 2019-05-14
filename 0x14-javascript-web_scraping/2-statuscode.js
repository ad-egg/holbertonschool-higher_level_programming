#!/usr/bin/node
// displays the status code of a GET request
const args = process.argv;
const req = require('request');
let url = args[2];
req.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
