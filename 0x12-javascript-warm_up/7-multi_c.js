#!/usr/bin/node
const process = require('process');
const args = process.argv;
let myNumber = args[2];
if (myNumber) {
  myNumber = Number(myNumber);
  if (isNaN) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < myNumber; i++) {
      console.log('C is fun');
    }
  }
}
