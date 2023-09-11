#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else if (process.argv[2]) {
  console.log('My number:' + ' ' + Math.floor(Number(process.argv[2])));
} else if (!process.argv[2]) {
  console.log('Not a number');
}
