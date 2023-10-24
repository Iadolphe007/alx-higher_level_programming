#!/usr/bin/node

const request = require('request')
url = `https://swapi-api.alx-tools.com/api/films/${mvId}`
mvId = process.argv[2]

request.get(url, (error, response, body) => {
    if (error) {
        console.log(error)
    } else {
        const data = JSON.parse(body)
        console.log(data.title)
    }
})