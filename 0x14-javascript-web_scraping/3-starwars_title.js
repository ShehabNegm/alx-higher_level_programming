#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (err, res, body) {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body).title);
});
