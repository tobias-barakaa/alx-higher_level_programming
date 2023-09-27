#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 100-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message); // Log a meaningful error message
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('HTTP Request Failed with Status Code:', response.statusCode); // Log a meaningful error message
    process.exit(1);
  }

  const movieData = JSON.parse(body);

  if (!movieData.characters || movieData.characters.length === 0) {
    console.log('No characters found for this movie.');
    process.exit(0);
  }

  // Fetch and print character names
  fetchAndPrintCharacterNames(movieData.characters);
});

function fetchAndPrintCharacterNames(characterUrls) {
  const characters = [];

  // Function to fetch character names from their URLs
  function fetchCharacterName(url) {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        characters.push(characterData.name);
        // If all characters are fetched, print them
        if (characters.length === characterUrls.length) {
          characters.forEach((character) => console.log(character));
        }
      } else {
        console.error('Error fetching character:', error ? error.message : 'Unknown error'); // Log a meaningful error message
      }
    });
  }

  // Fetch names for all character URLs
  characterUrls.forEach((url) => fetchCharacterName(url));
}
