function solution(N: number): number {
  const binary_num = N.toString(2);

  let numArr = [];
  let temp = "";

  for (let num of binary_num) {
    //이미 temp에 적고 있을 때 numArr로 push
    // 끝을 닫는 것
    if (temp !== "" && num == "1") {
      numArr.push(temp);
      temp = "";
    }
    // 아무것도 적지 않고 있을 때 temp에 적기 시작
    // 위에서 닫았어도 새로 시작해야 한다. (10100..)
    if (temp == "" && num == "1") {
      temp += num;
    }
    // 적고 있을 때 0을 만나면 temp에 적음
    if (temp !== "" && num == "0") {
      temp += num;
    }
  }

  if (numArr.length == 0) {
    return 0;
  } else {
    let ansArr: number[] = [];
    numArr.map((element) => {
      ansArr.push(element.length - 1);
    });

    let maxNum = Math.max(...ansArr);

    return maxNum;
  }
}
