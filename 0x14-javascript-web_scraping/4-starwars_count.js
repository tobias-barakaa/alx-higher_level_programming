#!/usr/bin/node
// Extract the API URL from the command line argument
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
    if(error)
    {
        console.log(error)
    }
   const filmsData = JSON.parse(body);
    // Initialize a count variable
    let count = 0;
    // Loop through the films
    for (let i = 0; i < filmsData.results.length; i++) {
      const film = filmsData.results[i];
      // Loop through the characters in the current film
      for (let j = 0; j < film.characters.length; j++) {
        const characterUrl = film.characters[j];
        // Check if the character URL contains '/18/' to match character ID 18
        if (characterUrl.includes('18')) {
           count++;
        }
      }
    }
console.log(count);
});

