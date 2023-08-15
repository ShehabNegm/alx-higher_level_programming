#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(+process.argv[2])) {
  console.log('Missing number of occurrences');
} else if (process.argv.length === 3) {
  const num = process.argv[2];
  for (let i = 0; i < +num; i++) {
    console.log('C is fun');
  }
}
