N = int(input())
lhp  = list(map(int, input().split()))
gp = list(map(int, input().split()))

maxHP = 100
maxGP = 0

dp = [[0]*101 for _ in range(N+1)]

for i in range(1,  N+1):
    for j in range(1,101):
        if(j>=lhp[i-1]):
            a =  dp[i-1][j-lhp[i-1]] + gp[i-1]
            b = dp[i-1][j] 
            dp[i][j] = max(a,b)
        else:

            dp[i][j] = dp[i-1][j]

#print(dp)
print(dp[N][99])