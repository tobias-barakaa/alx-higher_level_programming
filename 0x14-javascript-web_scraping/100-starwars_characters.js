#!/usr/bin/node
// A script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

let filmChars = [];
const charNames = {};

request({ url: url, json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    filmChars = body.characters;
    const requests = filmChars.map((index) => {
      return new Promise((resolve, reject) => {
        request({ url: index, json: true }, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(body.name);
          }
        });
      });
    });

    Promise.all(requests)
      .then((names) => {
        names.forEach((name, index) => {
          getName(filmChars[index], name);
        });
      })
      .catch((err) => {
        console.error(err);
      });
  }
});

// function that prints the name of each character
function getName(url, name) {
  charNames[url] = name;
  if (Object.keys(charNames).length === filmChars.length) {
    filmChars.forEach((idx) => {
      console.log(charNames[idx]);
    });
  }
}
