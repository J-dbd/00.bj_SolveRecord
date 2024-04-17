# 문제별 메모

## array 응용

    ```javascript

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
``` - 1001 사이의 0을 구할 때 array.length로 카운트

## `Number`와 `1e+25`

javascript엔진은 매우 큰 수를 위와 같은 표기로 사용된다. 이 경우 숫자화 할 필요가 없으므로 문자열로 솟자를 처리한다.
Number()를 사용하면 자동으로 큰 숫자를 저런 표기법으로 변환한다.
