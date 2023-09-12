#!/usr/bin/node
const process = require('process');
const args = process.argv;
let squareSize = args[2];

if (squareSize) {
  squareSize = Number(squareSize);

  if (isNaN(squareSize)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < squareSize; i++) {
      let row = 'x';

      for (let j = 1; j < squareSize; j++) {
        row += 'x';
      }

      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}
