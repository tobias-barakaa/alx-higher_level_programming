#!/usr/bin/node

const request = require('request');

// Create an empty object to store character names
const characterNames = {};

// Get the list of character URLs from the `/films/:id/` endpoint
request.get('https://swapi.dev/api/films/3/characters', (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const characterUrls = JSON.parse(body).results;

  // Fetch and print character names
  fetchAndPrintCharacterNames(characterUrls);
});

// Function to fetch and print character names
async function fetchAndPrintCharacterNames(characterUrls) {
  // Iterate over the character URLs and fetch the character name for each URL
  for (const characterUrl of characterUrls) {
    // Make an HTTP GET request to the character URL
    const response = await request.get(characterUrl);

    // Check if the response status code is 200 OK
    if (response.statusCode === 200) {
      // Parse the JSON response from the API
      const characterData = JSON.parse(response.body);

      // Add the character name to the object
      characterNames[characterUrl] = characterData.name;
    } else {
      console.error(error);
    }
  }

  // Once all character names have been fetched, print them to the console
  for (const characterUrl in characterNames) {
    console.log(characterNames[characterUrl]);
  }
}
