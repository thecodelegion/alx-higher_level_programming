#!/usr/bin/node
const process = require('process');
const args = process.argv;

function add(a, b) {
  if (args.length < 4) {
    console.error('Not enough command-line arguments provided.');
    return NaN;
  }

  a = args[2];
  b = args[3];

  const sum = Number(a) + Number(b);
  return sum;
}

const result = add();
console.log(result);
