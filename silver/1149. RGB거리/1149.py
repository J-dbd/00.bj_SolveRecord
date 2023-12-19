import sys
N = int(input())
rgb_arr = []
for i in range(N):
    rgb_arr.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]*(N+1) for _ in range(3)]

for i in range(1, N):
    rgb_arr[i][0] = min(rgb_arr[i-1][1], rgb_arr[i-1][2]) + rgb_arr[i][0]
    rgb_arr[i][1] = min(rgb_arr[i-1][0], rgb_arr[i-1][2]) + rgb_arr[i][1]
    rgb_arr[i][2] = min(rgb_arr[i-1][0], rgb_arr[i-1][1]) + rgb_arr[i][2]

print(rgb_arr)
