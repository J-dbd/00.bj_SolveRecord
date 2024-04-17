// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A: number[]): number {
  // Implement your solution here

  const maxNum = Math.max(...A);
  let checker = new Array(maxNum + 1).fill(0);

  for (let num of A) {
    const idx = num;
    checker[idx] += 1;
  }

  return findAnswer(checker);
}

const findAnswer = (checker: number[]): number => {
  //console.log(checker)
  for (let i = 0; i < checker.length; i++) {
    if (checker[i] == 0) continue;
    if (checker[i] % 2 == 1) {
      return i;
    }
  }
};
