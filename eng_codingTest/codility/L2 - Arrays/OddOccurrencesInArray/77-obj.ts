// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A: number[]): number {
  // Implement your solution here

  const maxNum = Math.max(...A);
  let checkerObj: Record<string, number> = {};

  for (let num of A) {
    const idx = num + "";
    if (!checkerObj.hasOwnProperty(idx)) {
      checkerObj[idx] = 1;
    } else {
      checkerObj[idx] += 1;
    }
  }

  let ans = 0;
  Object.entries(checkerObj).forEach(([k, v]) => {
    if (v !== 0 && v % 2 == 1) ans = parseInt(k);
  });

  return ans;
}
