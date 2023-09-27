#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
  console.error('Error: Please provide an API URL as the first command line argument.');
  process.exit(1);
}

// Send an HTTP GET request to the provided API URL
request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  // Parse the JSON response from the API
  const filmsData = JSON.parse(body);

  // Initialize a count variable to keep track of the number of characters
  let count = 0;

  // Loop through the films in the API response
  for (const film of filmsData.results) {
    // Loop through the characters in the current film
    for (const characterUrl of film.characters) {
      // Check if the character URL contains '18' (character ID 18)
      if (characterUrl.includes('18')) {
        // Increment the count if the character ID is 18
        count++;
      }
    }
  }

  // Print the total count of characters with ID 18
  console.log(count);
});
