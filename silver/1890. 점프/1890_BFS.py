#  BFS 를 사용하면 메모리 초과가 난다. 왜? q에 너무 많은 값이 들어가게 될 경우가...있음.
import sys
from collections import deque

N=int(input())
#그래프
graph=[[] for _ in range(N)]
#그래프에 데이터 넣음
for i in range(N):
    temp=list(map(int, sys.stdin.readline().strip().split()))
    graph[i].extend(temp)

cnt=0
#그래프 탐색을 위한 세팅
dx=[0,1]
dy=[1,0]

#BFS 사용
#출발점 넣어줌 
q=deque([[0,0]])


while q:
    #현재 위치 pick
    now=q.popleft()
    #현재 칸의 값(=위치의 이동 가능 거리) 추출
    dsize=graph[now[0]][now[1]]
    
    #추출한 현재 칸의 값이 0일 때 횟수를 늘리고 
    #다음 경로를 탐색하러 감
    if dsize==0:
        cnt+=1
        continue
    
    #현재 좌표 추출
    current_x, current_y=now[0], now[1]
    
    #그래프 탐색
    for i in range(2):
        next_x, next_y=current_x+(dx[i]*dsize), current_y+(dy[i]*dsize)
        
        if 0<=next_x<4 and 0<=next_y<4: #그래프 내의 범위 체크
            #다음 이동 좌표가 범위에 있을 때 스택에 삽입
            q.append([next_x, next_y])

print(cnt)


            