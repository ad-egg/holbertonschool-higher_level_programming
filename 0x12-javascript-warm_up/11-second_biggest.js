#!/usr/bin/node
// prints the second biggest integer in list of arguments
const args = process.argv;
if (args.length <= 3) { console.log('0'); } else { let sortedValues = args.slice(2).sort(); console.log(sortedValues[sortedValues.length - 2]); }
