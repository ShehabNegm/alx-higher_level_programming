#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  let num = number + 1;
  theFunction(num);
};
