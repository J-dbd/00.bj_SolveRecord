import sys 
N=int(input())

#계단 숫자 초기화
strs=[0]*301

#1층은 첫번째 인덱스에 저장
for i in range(1, N+1):
    strs[i]=int(sys.stdin.readline().strip())

#dp 배열 관리(세팅)
#dp[n]=n번째 게단에 올라갔을 때 얻을 수 있는 점수의 최댓값
dp = [0]*301
# dp[n-3]이 있기 때문에 1,2,3,층은 dp초기화가 필수
dp[1]=strs[1]
dp[2]=strs[1]+strs[2]
dp[3]=max(strs[1]+strs[3], strs[2]+strs[3])

#점화식 계산
for i in range(4, N+1):
    # n-1번째 게단으로 오는 경우는 n-3번째 계단으로 오는 경우도 포함(직전칸에서 올라온 경우의 최댓값)
    # n-2번째 계정을 밟고 온다면 3번째 계단은 밟지 않음.(전전칸에서 올라온 경우의 최댓값)
    # 둘 중 큰 값을 더해주면서 온다. 
    dp[i] = max(dp[i-3]+strs[i-1]+strs[i], dp[i-2]+strs[i])
    
print(dp[N])

