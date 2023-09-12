#!/usr/bin/node
const process = require('process');
const args = process.argv;
let firstArgumrnt, secondArgument;
if (args.length > 2) {
  firstArgumrnt = args[2];
  secondArgument = args[3];
}
console.log(firstArgumrnt + 'is' + secondArgument);
