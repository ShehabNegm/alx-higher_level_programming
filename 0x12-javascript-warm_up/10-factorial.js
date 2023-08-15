#!/usr/bin/node
function fac (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else {
    return a * fac(a - 1);
  }
}
console.log(fac(Number(process.argv[2])));
