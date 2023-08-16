#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let oc = 0;
  for (const item of list) {
    if (item === searchElement) {
      oc++;
    }
  }
  return oc;
};
