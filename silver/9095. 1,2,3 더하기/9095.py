#dp문제
T = int(input())

tests = [int(input()) for _ in range(T)]

maxTest = max(tests)

#print(maxTest)

dp = [0 for _ in range(maxTest+1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, maxTest+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

#print(dp, tests)
for test in tests:
   # print("test? ", test)
    print(dp[test])