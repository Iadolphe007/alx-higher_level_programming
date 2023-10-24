#!/usr/bin/node

const request = require('request');
const mvId = process.argv[2];
const url = `https://swapi.dev/api/films/${mvId}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
