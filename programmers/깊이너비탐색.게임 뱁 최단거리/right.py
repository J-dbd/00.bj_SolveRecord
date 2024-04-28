from collections import deque
def solution(maps):
    answer = 0
    n = len(maps[0]) #가로, y로 쓰임
    m = len(maps) #세로, x로 쓰임 (인덱싱 순서 때문에)
    #최단거리, BFS, Queue
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    origin = maps[m-1][n-1]
    def bfs(startAt):
        q = deque([startAt])
        while q:
            currX, currY = q.popleft()

            for i in range(4):
                nextX, nextY = currX+dx[i], currY+dy[i]

                #이동조건
                # 맵의 범위를 벗어나지 않을 것
                # 가본 곳이 아닌 곳
                # 벽이 아닌 곳
                if(nextX<0 or nextX>=m or nextY<0 or nextY>=n): continue # 맵의 범위를 벗어나면 continue
                if(maps[nextX][nextY]==0): continue  # 벽일 경우 continue
                
                if(maps[nextX][nextY] ==1): 
                    maps[nextX][nextY]= maps[currX][currY]+1
                    q.append([nextX, nextY])
                    
        #return maps[m-1][n-1]
    bfs([0,0])
    
    endpoint = maps[m-1][n-1]
    if(origin==endpoint):
        answer = -1
    else:
        answer = endpoint
    
    return answer

