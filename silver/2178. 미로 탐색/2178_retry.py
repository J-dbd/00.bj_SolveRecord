import sys
from collections import deque
N, M = list(map(int, input().split()))

graph = []
field = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    field.append(list(map(int, sys.stdin.readline().strip())))
    
queue = deque([[0,0]])

while queue:
    #print(queue.popleft())
    currX, currY = queue.popleft()
    
    for i in range(4):
        nextX, nextY = currX+dx[i], currY+dy[i]
        
        isInside = (nextX>=0 and nextX<N) and (nextY>=0 and nextY<M)
        
        if(isInside and field[nextX][nextY])==1:
            field[nextX][nextY] = field[currX][currY]+1
            queue.append([nextX, nextY])

print(field[N-1][M-1])