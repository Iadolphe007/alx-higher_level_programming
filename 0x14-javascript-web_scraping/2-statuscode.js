#!/usr/bin/node

const request = require('request');
const httpUrl = process.argv[2];

request.get(httpUrl, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
