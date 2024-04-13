import sys
from collections import deque


N = int(input())

field =[]
for i in range(N): field.append(list(map(int, sys.stdin.readline().strip())))



dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

groups = []

def searching_bfs(x, y):
    queue = deque([[x, y]])
    field[x][y] = 0 #방문했으므로 1로
    cnt = 1
    
    while queue:
        currX, currY = queue.popleft()
        
        for i in range(4):
            nextX, nextY = currX+dx[i], currY+dy[i]
            
            if(0<=nextX<N and 0<=nextY<N):
                if(field[nextX][nextY]==1):
                    field[nextX][nextY] = 0 #KEY: 방문한 곳을 0으로 만든다
                    cnt+=1
                    queue.append([nextX, nextY])
    return cnt

for i in range(N):
    for j in range(N):
        if(field[i][j]==1): #방문 여부 체크
            res = searching_bfs(i,j)
            if(res!=0):groups.append(res) #단지에 삽입
        


groups.sort()
print(len(groups))
print(*groups, sep='\n')
