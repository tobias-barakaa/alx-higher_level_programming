#!/usr/bin/node

const request = require('request');
// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Send an HTTP GET request to the API
request(apiUrl, async (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit(1);
  }

  // Check if the response status code is 200 OK
  if (response.statusCode !== 200) {
    console.log(response.statusCode);
    process.exit(1);
  }

  // Parse the JSON response from the API
  const movieData = JSON.parse(body);

  // Check if the movie has any characters
  if (!movieData.characters || movieData.characters.length === 0) {
    console.log(error);
    process.exit(0);
  }

  // Fetch and print character names
  await fetchAndPrintCharacterNames(movieData.characters);
});

// Function to fetch and print character names
async function fetchAndPrintCharacterNames(characterUrls) {
  // Create an empty array to store the fetched character names
  const characters = [];

  // Iterate over the character URLs and fetch the character name for each URL
  for (const characterUrl of characterUrls) {
    // Make an HTTP GET request to the character URL
    const response = await request(characterUrl);

    // Check if the response status code is 200 OK
    if (response.statusCode === 200) {
      // Parse the JSON response from the API
      const characterData = JSON.parse(response.body);

      // Add the character name to the array of fetched character names
      characters.push(characterData.name);
    } else {
      console.log(error);
    }
  }

  // Once all character names have been fetched, print them to the console
  characters.forEach((character) => console.log(character));
}
