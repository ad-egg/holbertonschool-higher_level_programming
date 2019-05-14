#!/usr/bin/node
// reads and prints the content of a file
const args = process.argv;
const fs = require('fs');
fs.readFile(args[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else { console.log(data); }
});
