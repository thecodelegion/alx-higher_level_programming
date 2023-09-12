#!/usr/bin/node
const process = require('process');
const args = process.argv;
const myNumber = args[2];
if (myNumber) {
  const number = Number(myNumber);
  if (isNaN(number)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + number);
  }
}
