import sys

N, K = list(map(int, input().split()))

wi =[]
pi =[]
for _ in range(N):
    w, p = list(map(int, input().split()))
    wi.append(w)
    pi.append(p)
    

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if(j>=wi[i-1]):
            a = pi[i-1] + dp[i-1][j-wi[i-1]]
            b = dp[i-1][j]
            dp[i][j] = max(a, b)
        
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])