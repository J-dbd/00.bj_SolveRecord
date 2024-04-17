// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A: number[]): number {
  // Implement your solution here
  // 1. sorting
  A.sort((a, b) => a - b);
  // 2. step in range 2, comapre next one from 0
  for (let i = 0; i < A.length; i += 2) {
    if (A[i + 1] != A[i]) {
      return A[i];
    }
  }
}

function solutionByXOR(A: number[]): number {
  // Implement your solution here
  let result = 0;

  for (let num of A) {
    result = result ^ num;
  }

  return result;
}
