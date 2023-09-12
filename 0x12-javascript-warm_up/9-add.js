#!/usr/bin/node
function add (a, b) {
  const process = require('process');
  const args = process.argv;
  a = args[2];
  b = args[3];
  const sum = Number(a) + Number(b);
  console.log(sum);
  return sum;
}
