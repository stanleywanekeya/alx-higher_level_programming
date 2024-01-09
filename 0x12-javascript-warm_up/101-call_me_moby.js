#!/usr/bin/node

exports.multFunc = (a, func) => {
  for (let i = 0; i < a; ++i) {
    func();
  }
};
