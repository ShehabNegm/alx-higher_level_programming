#!/usr/bin/node
exports.converter = function (base) {
  return function (numBase) {
    return numBase.toString(base);
  };
};
