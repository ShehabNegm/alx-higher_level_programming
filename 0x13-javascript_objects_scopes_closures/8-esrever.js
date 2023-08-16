#!/usr/bin/node
exports.esrever = function (list) {
  const rList = [];
  while (list.length) {
    rList.push(list.pop());
  }
  return rList;
};
