#!/usr/bin/node

const request = require("request");
const url = process.argv[2];

request(url, (err,data) => {
  if(err)
        console.log(error.message);
  else 
        console.log(`code: ${data.statusCode}`)
