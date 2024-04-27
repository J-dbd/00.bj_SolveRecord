from collections import deque
def solution(maps):
    answer = 0
    m = len(maps) #세로 
    n = len(maps[0]) #가로
    
    #최단거리, BFS, Queue
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    origin = maps[m-1][n-1]
    
    routes=[]
    ans = 0 
    
    
    def bfs(startAt):
        q = deque([startAt])
        print(q)
        cnt = 0
        while q:
            cnt+=1
            if(cnt>=50):
                break
            currX, currY = q.popleft()
            
            for i in range(4):
                nextX, nextY = currX+dx[i], currY+dy[i]

                #이동조건
                # 맵의 범위를 벗어나지 않을 것
                # 가본 곳이 아닌 곳
                # 벽이 아닌 곳
                #rule = (0<=nextX<n) and (0<=nextY<m) #맵 범위
                rule1 = (maps[nextX][nextY]!=0) #벽이 아닌 곳
                rule2 = maps[nextX][nextY]==1 #처음 지나가는 길
                
                if(nextX<0 or nextY<0 or nextX>n or nextX>m): continue
                
                if(rule1 and rule2):
                    maps[nextX][nextY]=maps[currX][currY]+1
                    q.append([nextX, nextY])
                    

    bfs([0,0])
    print(maps)
    #     print(maps)
    # print("?", maps[m-1][n-1])
    # endpoint = (maps[m-1][n-1])+1
    # if(origin==endpoint):
    #     answer = -1
    # else:
    #     answer = endpoint
    
    
    
    return answer

