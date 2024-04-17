function solution(N: number): number {
  const binary_num = N.toString(2);

  let numArr = [];

  let temp = "";

  for (let num of binary_num) {
    if (temp !== "" && num == "1") {
      numArr.push(temp);
      temp = "";
    }

    if (temp == "" && num == "1") {
      temp += num;
    }

    if (temp !== "" && num == "0") {
      temp += num;
    }
  }

  if (numArr.length == 0) {
    return 0;
  } else {
    let ansArr: number[] = [];
    numArr.map((element) => {
      ansArr.push(Number(element));
    });

    let maxNum = Math.max(...ansArr);
    const maxNumArr = Array.from(maxNum + "");

    return maxNumArr.length - 1;
  }
}

/** 
   * 
   * num: 1 | temp:1 | idx 1
num: 1 | temp:1 | idx 2
num: 0 | temp:10 | idx 3
num: 0 | temp:100 | idx 4
num: 0 | temp:1000 | idx 5
num: 0 | temp:10000 | idx 6
num: 0 | temp:100000 | idx 7
num: 0 | temp:1000000 | idx 8
num: 0 | temp:10000000 | idx 9
num: 0 | temp:100000000 | idx 10
num: 0 | temp:1000000000 | idx 11
num: 0 | temp:10000000000 | idx 12
num: 0 | temp:100000000000 | idx 13
num: 0 | temp:1000000000000 | idx 14
num: 0 | temp:10000000000000 | idx 15
num: 0 | temp:100000000000000 | idx 16
num: 0 | temp:1000000000000000 | idx 17
num: 0 | temp:10000000000000000 | idx 18
num: 0 | temp:100000000000000000 | idx 19
num: 0 | temp:1000000000000000000 | idx 20
num: 0 | temp:10000000000000000000 | idx 21
num: 0 | temp:100000000000000000000 | idx 22
num: 0 | temp:1000000000000000000000 | idx 23
num: 0 | temp:10000000000000000000000 | idx 24
num: 0 | temp:100000000000000000000000 | idx 25
num: 0 | temp:1000000000000000000000000 | idx 26
num: 0 | temp:10000000000000000000000000 | idx 27
num: 1 | temp:1 | idx 28
num: 0 | temp:10 | idx 29
num: 1 | temp:1 | idx 30
[ 1, 1e+25, 10 ]
1e+25
5
4
   * 
   */
