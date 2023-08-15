#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const num = number + 1;
  theFunction(num);
};
