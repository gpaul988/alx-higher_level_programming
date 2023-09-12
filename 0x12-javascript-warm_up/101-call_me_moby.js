#!/usr/bin/node
// Graham S. Paul (101-call_me_moby.js)

exports.callMeMoby = (x, cb) => {
  for (let i = 0; i < x; i++) {
    cb();
  }
};
