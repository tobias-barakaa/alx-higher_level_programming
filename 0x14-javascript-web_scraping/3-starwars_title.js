#!/usr/bin/node

const request = require('request');

// Extract the movie ID from the command line argument
const movieID = process.argv[2];

// Define the API endpoint URL with the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  // Check if the response status code is 200 (OK)
  if (response.statusCode === 200) {
    try {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } catch (parseError) {
      console.log(parseError);
    }
  } else {
    console.log(response.statusCode);
  }
});
