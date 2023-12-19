import sys
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0] *(N+1)

dp[0] = nums[0]

for i in range(1, N+1):
    for j in range(1, i):
        dp[i] = max(dp[i-1] + nums[j], nums[j-1] + nums[j])



if(N>=2):
    dp.pop(1)
else:
    pass


#print(dp)
print(max(dp))

##시간 초과