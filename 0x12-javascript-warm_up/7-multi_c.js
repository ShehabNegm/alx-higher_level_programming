#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else if (process.argv.length === 3) {
  const num = process.argv[2];
  if (isNaN(+num)) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < +num; i++) {
      console.log('C is fun');
    }
  }
}
