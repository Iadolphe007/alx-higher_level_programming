#!/usr/bin/node

const x = Math.floor(Number(process.argv[2]));
if (!process.argv[2]) {
  console.log('Missing size');
} else if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (let j = 0; j < x; j++) {
  let size = ' ';
  for (let i = 0; i < x; i++) {
    size += 'x';
  }
  console.log(size);
}
