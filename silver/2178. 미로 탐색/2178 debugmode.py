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
cnt=0

while queue:
    print(f'{cnt}번째 queue: {queue}')
    current_x, current_y=queue.popleft()
    
    #이동 탐색
    for i in range(4):
        print(f'    next_x = {current_x} + {dx[i]}', end=' / ')
        print(f'    next_y = {current_y} + {dy[i]}')
        next_x, next_y = current_x+dx[i], current_y+dy[i]
        
        if 0<=next_x<N and 0<=next_y<M:
            print(f'        graph[{next_x}][{next_y}]={graph[next_x][next_y]}')
            if graph[next_x][next_y] ==1:
                queue.append((next_x, next_y))
                graph[next_x][next_y]=graph[current_x][current_y]+1 
    
    cnt+=1
    print(". . . . . . . . . . . ")
    
print(graph[N-1][M-1])



'''
[
    [1, 0, 1, 1, 1, 1], 
    [1, 0, 1, 0, 1, 0], 
    [1, 0, 1, 0, 1, 1], 
    [1, 1, 1, 0, 1, 1]
    ]

[
    [3, 0, 9, 10, 11, 12], 
    [2, 0, 8, 0, 12, 0], 
    [3, 0, 7, 0, 13, 14], 
    [4, 5, 6, 0, 14, 15]
    ]

'''
