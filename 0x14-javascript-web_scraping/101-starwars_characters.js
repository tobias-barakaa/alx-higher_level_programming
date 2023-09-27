#!/usr/bin/node

const request = require('request');

// Check if the user provided the Movie ID as a command line argument
if (process.argv.length !== 3) {
  console.error('Usage: node 101-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// Extract the Movie ID from the command line argument
const movieId = process.argv[2];

// Construct the URL for the movie's details
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Check if the response status code is 200 (OK)
  if (response.statusCode === 200) {
    try {
      const movieData = JSON.parse(body);

      // Check if the movie data contains a "characters" property
      if (Array.isArray(movieData.characters)) {
        // Display each character name
        movieData.characters.forEach((characterUrl) => {
          request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
              console.error('Error:', charError);
            } else if (charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
            }
          });
        });
      } else {
        console.log('No characters found for this movie.');
      }
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error:', response.statusCode);
  }
});
