import sys
from collections import deque


N = int(input())

#field = [[0]*(N) for _ in range(N)]
field =[]

for i in range(N):
    #print()
    field.append(list(map(int, sys.stdin.readline().strip())))


print(field)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

group = []
queue = deque([[0,0]])
def searching_bfs():
    
    while queue:
        currX, currY = queue.popleft()
  
        
        for i in range(4):
            nextX, nextY = currX+dx[i], currY+dy[i]
            
            if(0<=nextX<N and 0<=nextY<N):
                if(field[nextX][nextY]==1):
                    field[nextX][nextY] = field[currX][currY]+1
                    queue.append([nextX, nextY])
                    
                    
print(field)     
searching_bfs() 
print(field)                   