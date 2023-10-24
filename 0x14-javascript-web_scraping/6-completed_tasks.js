#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const completedTask = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!completedTask[todo.userId]) {
        completedTask[todo.userId] = 1;
      } else {
        completedTask[todo.userId] += 1;
      }
    }
  });
  console.log(completedTask);
});
