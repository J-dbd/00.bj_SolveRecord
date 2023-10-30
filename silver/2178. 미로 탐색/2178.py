import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().strip().split()))

graph=[[] for _ in range(N)]



for i in range(N):
    graph[i].extend(list(map(int, list(sys.stdin.readline().strip()))))

queue=deque([(0,0)])


#좌표 이동 
dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

while queue:
    current_x, current_y=queue.popleft()
    
    #이동 탐색
    for i in range(4):
        #이동할 좌표의 값과 현재 값을 더해서 현재 경로값을 누적
        next_x, next_y = current_x+dx[i], current_y+dy[i]
        
        #범위 내에 있는지 체크
        if 0<=next_x<N and 0<=next_y<M:
            
            if graph[next_x][next_y] ==1:
                #큐에 다음으로 이동할 경로를 넣어둠
                #여러 곳이 있어도 큐에 넣어놨으므로 같은 레벨 상의 노드로 이동 가능하다
                #즉, BFS 구현 가능
                queue.append((next_x, next_y))
                #범위 내에 있다면 누적한 경로 값을 그래프에 기입
                #즉 그 좌표까지의 누적 cost값으로 update 
                graph[next_x][next_y]=graph[current_x][current_y]+1 
    
    
print(graph[N-1][M-1])

