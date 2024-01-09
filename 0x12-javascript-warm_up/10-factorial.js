#!/usr/bin/node

const fact = Math.floor(Number(process.argv[2]));

function factorial (x) {
  if (isNaN(x)) return 1;
  if (x === 0) return 1;
  return x * factorial(x - 1);
}

console.log(factorial(fact));
