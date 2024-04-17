# error record:: `object` & `array`

```

big random test n=999,999, multiple repetitions

Detected time complexity: O(N\*\*2)

▶big1
big random test n=999,999, multiple repetitions✘RUNTIME ERROR
tested program terminated with exit code 1
1.0.252 sRUNTIME ERROR, tested program terminated with exit code 1
stderr:
RangeError: Maximum call stack size exceeded
at solution (solution.js:6:25)
at solutionWrapper (/tmp/exec_user_xtei6vpd/exec.js:337:28)
at /tmp/exec_user_xtei6vpd/exec.js:356:20

▶big2
big random test n=999,999✘RUNTIME ERROR
tested program terminated with exit code 1
1.0.272 sRUNTIME ERROR, tested program terminated with exit code 1
stderr:
RangeError: Maximum call stack size exceeded
at solution (solution.js:6:25)
at solutionWrapper (/tmp/exec_user_xtei6vpd/exec.js:337:28)
at /tmp/exec_user_xtei6vpd/exec.js:356:20
```

처음 선택한 방법은 배열을 사용했다.

1. 최대 값만큼의 수를 가진 배열을 선언
2. 배열 idx를 기준으로 +1하여 짝수가 아닌 것을 반환

런타임 에러가 났다.

다음 선택한 방법은 객체를 사용했다.

1. 입력된 배열을 순회하며 각 값을 key, key값이 없다면 1로 세팅. 있다면 +1 해주었다.
2. 이후 `Object.entries(obj)`와 `forEach`로 k 와 v를 순회하며 0이 아니고 나누어 1이 남는(홀수) 경우의 key값을 반환

런타임 에러가 났다.

이쯤되면 다른 방법이 있다고 느꼈다. 문제를 다시 보니 ..

```
N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,0  00,00  0,000];
all but one of the values in A occur an even number of times.
```

- **홀수인 N는 array의 갯수/길이(length)가 최대 백만**이 될 수 있다.
- array의 element 값은 최대 10억이 될 수 있다.
- 단 한개의 값을 제외한 array A의 값은 짝수 번 등장한다.

## Array의 size가 백만이 될 수 있다

O(n) 방법으로 풀어야 한다. 왜냐하면 O(n2) 으로 작동한다면 최대 백만\*백만 ..이 되어 너무 느려진다.

## Array의 element 값이 최대 10억이 될 수 있다.

성능 저하 없이 연산을 수행해야 하는데, 최신 프로그래밍 언어나 보통 32비트 정수는 대략 21억까지 값을 처리할 수 있다.

# 풀이 방법

## XOR 연산

XOR 연산은 두 비트가 서로 다를 때 1을 반환하고, 같을 때 0을 반환하는 비트 단위의 연산이다. 이로인해 XOR 연산을 사용하면 중간에 같은 숫자가 등장하면 그 숫자는 자동적으로 상쇄되고, 결국 남는 숫자는 한 번만 등장한 숫자만 남는다. 즉, pairing 문제에 XOR연산을 사용하면 쌍을 이루는 숫자가 상쇄되고 쌍을 이루지 않은 단 하나만 빠르고 효과적으로(O(n)) 가져올 수 있다.

## sort, 간격 2씩 검사

O(n)으로 연산 가능
