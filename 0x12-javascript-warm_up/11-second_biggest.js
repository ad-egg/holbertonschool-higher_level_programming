#!/usr/bin/node
// prints the second biggest integer in list of arguments
let args = process.argv.slice(2);
if (args.length <= 1) {
  console.log('0');
} else {
  let sortedValues = new Set(args.sort());
  console.log(sortedValues[sortedValues.length - 2]);
}
