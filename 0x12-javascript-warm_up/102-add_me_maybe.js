#!/usr/bin/node
// Graham S. Paul (102-add_me_maybe.js)

exports.addMeMaybe = (num, cb) => {
  const newnum = num + 1;
  cb(newnum);
};
