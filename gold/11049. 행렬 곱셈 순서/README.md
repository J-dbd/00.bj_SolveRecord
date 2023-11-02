참조용 저장

```python
# DP
    dp = [[0]*N for _ in range(N)]
    for d in range(N):
        for i in range(N - d):
            j = i + d

            if i == j:
                continue

            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1]
                               [j] + nums[i]*nums[k+1]*nums[j+1])

    print(dp)
```
