#!/usr/bin/node

const x = parseInt(process.argv[2]);
if (isNaN(x) || x < 1) {
  console.log('Missing size');
} else {
  for (let j = 0; j < x; j++) {
    let size = ' ';
    for (let i = 0; i < x; i++) {
      size += 'X';
    }
    console.log(size);
  }
}
