#!/usr/bin/node

/* Graham S. Paul (6-completed_tasks.js)
 * Create script that computes the number
 * of tasks completed by user id. */

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const completedTask = {};
    const json = JSON.parse(body);

    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (completedTask[json[i].userId] === undefined) {
          completedTask[json[i].userId] = 0;
        }
        completedTask[json[i].userId]++;
      }
    }

    console.log(completedTask);
  } else {
    console.error('Error making the request:', error);
  }
});
