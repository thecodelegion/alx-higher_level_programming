#!/usr/bin/node
function add(a, b) {
  const process = require('process');
  const args = process.argv;
  let a = args[2];
  let b = args[3];
  const sum = Number(a) + Number(b);
  console.log(sum);
  return sum;
}
