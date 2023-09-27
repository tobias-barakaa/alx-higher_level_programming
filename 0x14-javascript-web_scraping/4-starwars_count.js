#!/usr/bin/node
// Extract the API URL from the command line argument
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
 try {
      const filmsData = JSON.parse(body).results;

      // Initialize a count variable
      let count = 0;
      for (const film of filmsData) {
        if (film.characters.includes('/18/')) {
          count ++;
        }
      }

      console.log(count);
    } catch (error) {
      console.log(error);
    } 
});
