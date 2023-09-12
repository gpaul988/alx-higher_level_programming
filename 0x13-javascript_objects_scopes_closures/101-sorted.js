#!/usr/bin/node
// Graham S. Paul (101-sorted.js)

const dict = require('./101-data').dict;

const newDic = {};
for (const key in dict) {
  if (newDic[dict[key]] === undefined) {
    newDic[dict[key]] = [];
  }
  newDic[dict[key]].push(key);
}

console.log(newDic);
