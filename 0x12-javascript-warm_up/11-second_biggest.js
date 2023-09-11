#!/usr/bin/node

const args = process.argv.slice(2);
function largestInt (numbers) {
  if (numbers.length < 2) {
    return 0;
  }
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const numStr of numbers) {
    const num = parseInt(numStr);
    if (!isNaN(num)) {
      if (num > largest) {
        secondLargest = largest;
        largest = num;
      } else if (num > secondLargest && num < largest) {
        secondLargest = num;
      }
    }
  }
  return secondLargest;
}
const secondLargest = largestInt(args);
console.log(secondLargest);
