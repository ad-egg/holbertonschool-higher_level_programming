#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let reps = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { reps++; }
  }
  return reps;
};
