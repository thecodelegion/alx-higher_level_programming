#!/usr/bin/node
const process = require('process');
const args = process.argv;
let firstArgument;
if(args.length > 2) {
	firstArgument = args[2];
} else {
	console.log('No argument');
}
if (firstArgument){
	console.log(firstArgument);
}
