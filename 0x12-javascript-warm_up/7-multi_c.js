#!/usr/bin/node

let x  = process.argv[2];
let i = 0;
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}
while (i < x) {
  console.log('C is fun');
  i++;
}
