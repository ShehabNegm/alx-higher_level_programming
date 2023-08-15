#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  let num = number++;
  theFunction(num);
};
