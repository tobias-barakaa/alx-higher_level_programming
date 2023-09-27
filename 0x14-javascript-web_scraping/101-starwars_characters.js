#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];

const baseUrl = 'https://swapi.dev/api/films/';

request(baseUrl + movieId, { json: true }, (err, res, filmData) => {
  if (err) {
    console.log(err);
  } else {
    const characterUrls = filmData.characters;
    // Function to fetch character names and print them
    function fetchAndPrintCharacterNames(urls, index = 0) {
      if (index < urls.length) {
        request(urls[index], { json: true }, (err, res, characterData) => {
          if (err) {
            console.log(err);
          } else {
            console.log(characterData.name);
            fetchAndPrintCharacterNames(urls, index + 1);
          }
        });
      }
    }

    fetchAndPrintCharacterNames(characterUrls);
  }
});
