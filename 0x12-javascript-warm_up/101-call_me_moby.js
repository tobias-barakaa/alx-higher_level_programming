#!/usr/bin/node
exports.callMeMoby = function (x, theFunc) {
  for (let i = 0; i < x; i++) {
    theFunc();
  }
};
