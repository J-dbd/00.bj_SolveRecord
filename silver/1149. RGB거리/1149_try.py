import sys
N = int(input())
rgb_arr = []
for i in range(N):
    rgb_arr.append(list(map(int, sys.stdin.readline().split())))

dp = [0]*(N+1)
print(rgb_arr)

#다 달라야 한다는 소리네 

for i in range(3):
    for j in range(0, N):
        if(i == 0):
            dp[0] = min(rgb_arr[j][0]+rgb_arr[j][1], rgb_arr[j][0]+rgb_arr[j][2])
        elif(i==1):
            dp[1] = min(rgb_arr[j][1]+rgb_arr[j][0], rgb_arr[j][1]+rgb_arr[j][2])
        elif(i==2):
            dp[2] = min(rgb_arr[j][2]+rgb_arr[j][0], rgb_arr[j][2]+rgb_arr[j][1])

print(dp)