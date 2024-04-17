// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');
//number[]
function solution(A: number[], K: number): number[] {
  // Implement your solution here
  //console.log("isArray ", Array.isArray(A), A)
  const len = A.length;

  let ans: number[] = new Array(len).fill(0);

  for (let i = 0; i < len; i++) {
    const ans_idx = getNextIdx(i, K, len);
    ans[ans_idx] = A[i];

    // console.log(`ans_idx :${ans_idx}| A[i]:${A[i]} |ans[ans_idx]:${ans[ans_idx]}`)
  }

  //console.log(`A: ${A} | ans: ${ans}`)

  return ans;
}

const getNextIdx = (idx: number, K: number, len: number): number => {
  let nextIdx = idx + K;

  if (nextIdx >= len) {
    nextIdx = nextIdx % len;
  }
  //console.log(`>>idx :${idx}| len: ${len} | nextIdx :${nextIdx}`)

  return nextIdx;
};
