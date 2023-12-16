import sys

#방법 3 
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp)) 
#print(dp)

#부분수열: seq를 지켜야 한다
#dp = [0]*(N+1)
# dp[0] = arr[0]

# for i in range(1, N+1):
#     target = max(arr[i-1], dp[i-1])
#     dp[i] = target

# print(len(set(dp)))


# 방법 1 : set 이용
# dp = set()
# dp.add(arr[0])
# for i in range(1, N):
#     target = max(max(dp), arr[i])
#     dp.add(target)

# print(len(dp))


