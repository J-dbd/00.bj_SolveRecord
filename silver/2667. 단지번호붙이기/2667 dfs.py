import sys
N = int(input())

graph = [ list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

groups = []

def dfs(x, y):
    stack = []
    graph[x][y] = 0
    stack.append([x,y])
    
    cnt = 1
    
    while stack:
        currX, currY =stack.pop()

        
        for i in range(4):
            nextX, nextY = currX+dx[i], currY+dy[i]
            
            if(0<=nextX<N and 0<=nextY<N):
                if(graph[nextX][nextY]==1):
                    graph[nextX][nextY] = 0
                    stack.append([nextX, nextY])
                    cnt +=1
    
    return cnt

for i in range(N):
    for j in range(N):
        if(graph[i][j]==1):
            groups.append(dfs(i,j))
            
groups.sort()
print(len(groups))
print(*groups, sep='\n')
            