#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const userId in dict) {
  const ocurrenceCount = dict[userId];
  if (ocurrenceCount in newDict) {
    newDict[ocurrenceCount].push(userId);
  } else {
    newDict[ocurrenceCount] = [userId];
  }
}
console.log(newDict);
