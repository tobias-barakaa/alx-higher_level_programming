#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const CHARACTER_ID = 18; // Wedge Antilles

function countMoviesWithCharacter(url, characterId) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      }

      const movies = JSON.parse(body).results;
      const moviesWithCharacter = movies.filter(movie => movie.characters.includes(characterId));

      resolve(moviesWithCharacter.length);
    });
  });
}

async function main() {
  const count = await countMoviesWithCharacter(API_URL, CHARACTER_ID);

  console.log(count);
}

main();
