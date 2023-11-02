import sys
from collections import deque

N=int(input())
#그래프
graph=[[] for _ in range(N)]
#그래프에 데이터 넣음
for i in range(N):
    temp=list(map(int, sys.stdin.readline().strip().split()))
    graph[i].extend(temp)
    
#dp
dp = [[0]*N for _ in range(N)]
dp[0][0]=1

## dp와 graph는 다르다! 
## dp에서는 최종 목적지까지 도달하는 경우의 수를 저장한다.
## 즉, (0, 0)에서 시작해 (n-1, n-1)까지 가는 경우의 수를 저장한다. 

for i in range(N):
    for j in range(N):
        dsize=graph[i][j] #이동 가능한 거리의 크기
        
        if dsize==0: #마지막 종착지에 도착했을 때 감지
            break
        
        next_x=i+dsize
        next_y=j+dsize

        
        if next_x<N:
            dp[next_x][j]+=dp[i][j] #여기까지 온 걸 더해준다.
        
        if next_y<N:
            dp[i][next_y]+=dp[i][j]
            

#print(dp)

print(dp[N-1][N-1])
