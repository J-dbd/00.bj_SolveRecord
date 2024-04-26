from collections import deque
def solution(maps):
    answer = 0
    m = len(maps) #세로 
    n = len(maps[0]) #가로
    
    #최단거리, BFS, Queue
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    
    ans = 0 
    def bfs(startAt):
        q = deque([startAt])
        print(q)
        cnt = 0
        while q:
            cnt+=1
            # if(cnt>=10):
            #     break
            currX, currY = q.popleft()
            #print("현재 위치: ", currX, currY,  maps[currX][currY])
            
            for i in range(4):
                nextX, nextY = currX+dx[i], currY+dy[i]
                #print("후보: ", nextX, nextY)
                
                #이동조건
                # 맵의 범위를 벗어나지 않을 것
                # 가본 곳이 아닌 곳
                # 벽이 아닌 곳
                rule = (0<=nextX<n) and (0<=nextY<m-1)
                rule1 = maps[nextX][nextY]!=0 #벽
                rule2 = maps[nextX][nextY]==1 #가보지 않은 길일 것
                
                if(rule and rule1):
                    
                    print("이동할 좌표 ", nextX, nextY, "현재 count", maps[currX][currY])

                    if(rule2):#아직 안가본 길, 즉 다음 길이 1일 때
                        maps[nextX][nextY] += maps[currX][currY] #지금까지 온 길 횟수 더해줌
                        q.append([nextX, nextY])
                    else:#가본 길인데? 즉 다음 maps 값이 1이 아닐 때
                        maps[nextX][nextY] = maps[currX][currY] 
                        
                        
                    
            
        
    bfs([0,0])
    print(maps[m-1][n-1])
    
    return answer

# >> visited를 쓰자