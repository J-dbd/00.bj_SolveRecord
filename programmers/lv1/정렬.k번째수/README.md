kit-정렬

# python vs javascript [ 배열 ]

`sort()`사용시 javascript의 경우 문자열로 변환, 사전순으로 정렬한다. 따라서, 2와 100 중 문자 100과 문자 2 사이에서 1이 2보다 앞서기 때문에 100, 2 이런 순서대로 정렬이 된다.

## 방지방법

```javascript
sort((a, b) => a - b);
// 익명함수를 만들어 넣어준다.
```
