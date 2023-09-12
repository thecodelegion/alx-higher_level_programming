#!/usr/bin/node
const process = required('process');
const args = process.argv;
let myNumber = args[2];
if (myNumber) {
  myNumber = Number(myNumber);
  if (isNaN) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + myNumber);
  }
}
