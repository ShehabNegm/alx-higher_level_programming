#!/usr/bin/node
function add (a, b) {
  const sum = +a + +b;
  return console.log(sum);
}
add((process.argv[2]), (process.argv[3]));
