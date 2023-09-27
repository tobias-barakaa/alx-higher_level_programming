#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Send an HTTP GET request to the provided API URL
request(apiUrl, (error, response, body) => {
   // Parse the JSON response from the API
   const filmsData = JSON.parse(body);

   // Initialize a count variable to keep track of the number of characters
   let count = 0;

   // Loop through the films in the API response
   for (let i = 0; i < filmsData.results.length; i++) {
      const film = filmsData.results[i];

      // Loop through the characters in the current film
      for (let j = 0; j < film.characters.length; j++) {
        const characterUrl = film.characters[j];

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
