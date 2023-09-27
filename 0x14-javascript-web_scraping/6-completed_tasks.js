#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

// Initialize an empty object to store completed task counts by user ID
const completedTasksByUser = {};

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit(1);
  }
const todos = JSON.parse(body);

  // Iterate through the todos and count completed tasks by user
  for (const todo of todos) {
    if (todo.completed) {
      const userId = todo.userId;
      completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
    }
  }

  // Print the completed tasks by user as a JSON object
  console.log(completedTasksByUser);
});
