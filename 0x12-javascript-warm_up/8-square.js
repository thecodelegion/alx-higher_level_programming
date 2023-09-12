#!/usr/bin/node
const process = require('process');
const args = process.argv;
let squareSize = args[2];
if (squareSize) {
  squareSize = Number(squareSize);
  if ((squareSize = NaN)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < squareSize; i++) {
      console.log('x');
      for (let j = 1; j < squareSize; j++) {
        console.log('x', (end = ''));
      }
    }
  }
}
