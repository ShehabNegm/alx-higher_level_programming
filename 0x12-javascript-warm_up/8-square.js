#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(+process.argv[2])) {
  console.log('Missing size');
} else if (process.argv.length === 3) {
  const num = process.argv[2];
  const sqr = 'x';
  const str = sqr.repeat(+num);
  for (let i = 0; i < +num; i++) {
    console.log(str);
  }
}
