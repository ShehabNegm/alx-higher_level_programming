#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const num = number++;
  theFunction(num);
};
