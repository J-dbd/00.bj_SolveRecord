function solution(N) {
  // Implement your solution here
  const binary_num = N.toString(2);

  let maxGap = 0;
  let isCounting = false;
  let countingNum = 0;
  let cnt = 0;
  for (let num of binary_num) {
    if (isCounting == false && num === "1") {
      isCounting = true;
      countingNum += 1;
    } else if (isCounting == true && num == "0") {
      cnt += 1;
    } else if (isCounting == true && num == "1") {
      isCounting = false;

      if (cnt > maxGap) {
        maxGap = cnt;
      }
    }

    console.log(
      `num: ${num} | isCounting:${isCounting} | maxGap:${maxGap} | cnt:${cnt}`
    );
  }

  if (countingNum !== 0) {
    return maxGap;
  } else {
    return 0;
  }
}

solution(328);
//console.log("보임?");
