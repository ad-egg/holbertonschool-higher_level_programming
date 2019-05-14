#!/usr/bin/node
// writes a string to a file
const args = process.argv;
const fs = require('fs');
let filepath = args[2];
let string = args[3];
fs.writeFile(filepath, string, 'utf8', function (err) {
  if (err) { console.log(err); }
});
