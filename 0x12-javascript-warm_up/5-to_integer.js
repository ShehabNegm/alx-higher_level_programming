#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (process.argv.length === 3) {
  const num = process.argv[2];
  if (isNaN(+num)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${Math.trunc(+num)}`);
  }
}
