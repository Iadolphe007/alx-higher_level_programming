#!/usr/bin/node

const x = process.argv[2];
if (!x) {
  console.log('Missing size');
} else if (isNaN(x)) {
  console.log('Missing size');
}
for (let j = 0; j < x; j++) {
  let size = ' ';
  for (let i = 0; i < x; i++) {
    size += 'x';
  }
  console.log(size);
}
