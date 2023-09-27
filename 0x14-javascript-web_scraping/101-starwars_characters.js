#!/usr/bin/node

const request = require('request');

// Check if the movie ID is provided
if (!process.argv[2]) {
  console.error('Error: Please provide a movie ID as the first command line argument.');
  process.exit(1);
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Send an HTTP GET request to the API
request(apiUrl, { json: true }, async (error, response, filmData) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  // Get the list of character URLs
  const characterUrls = filmData.characters;

  // Function to fetch and print character names
  async function fetchAndPrintCharacterNames(urls, index = 0) {
    if (index < urls.length) {
      // Make an HTTP GET request to the character URL
      const response = await request(urls[index], { json: true });

      // Check if the response status code is 200 OK
      if (response.statusCode === 200) {
        // Parse the JSON response from the API
        const characterData = JSON.parse(response.body);

        // Print the character name to the console
        console.log(characterData.name);

        // Recursively fetch and print the next character name
        await fetchAndPrintCharacterNames(urls, index + 1);
      } else {
        console.error(error);
      }
    }
  }

  // Fetch and print the character names
  await fetchAndPrintCharacterNames(characterUrls);
});
