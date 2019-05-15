#!/usr/bin/node
// computes the number of tasks completed by user id
const args = process.argv;
const req = require('request');
let url = args[2];
req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let tasks = JSON.parse(body);
    let answer = {};
    for (let task of tasks) {
      if (task.completed === true) {
        if (answer[task.userId] == null) {
          answer[task.userId] = 1;
        } else {
          answer[task.userId]++;
        }
      }
    }
    console.log(answer);
  }
});
