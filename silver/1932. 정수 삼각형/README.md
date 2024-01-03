# 1932 번: 정수 삼각형 (실버 1)

틀린 이유:

1. 누적합 종류는 dp를 새로 선언하여 만드는 것보다는 주어진 값을 그대로 이용하는 게 좋다!
2. 위치별로 분화를 좀 더 세세히.

- 내가 풀던 코드 기록

```python
dp = [0]*5 / dp[i] = max(dp[i-1] + ta[i][j-1], dp[i-1] + ta[i][j])

#당장 합이 커지지만, 거시적으로 봤을 때 다른 경로로의 선택을 완전히 외면하고 가기에 챙길 수 없다


for i in range(1, T):
    for j in range(len(dp[i])):
        if(j==1):
            dp[i][j] = max(dp[i-1][j] + ta[i][0], dp[i-1][j] + ta[i][1])
        else:
            dp[i][j] = max(dp[i-1][j] + ta[i][j-1], dp[i-1][j] + ta[i][j])

        dp[i][j] = max(dp[i-1][j] + ta[i][j-1], dp[i-1][j] + ta[i][j])
        dp[i][j] = dp[i-1][j] + ta[i][j-1]


```
