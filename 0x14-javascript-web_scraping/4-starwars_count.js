#!/usr/bin/node
const request = require('request');

// Extract the API URL from the command line argument
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const characterId = 18;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {

  // Check if the response status code is 200 (OK)
  if (response.statusCode === 200) {
    try {
      const filmsData = JSON.parse(body);

      // Initialize a count variable
      let count = 0;

      // Loop through the films and count the occurrences of Wedge Antilles
      for (const film of filmsData) {
        if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          count++;
        }
      }

      console.log(count);
    } catch (parseError) {
      console.log(parseError);
    }
  } else {
    console.log(response.statusCode);
  }
});
