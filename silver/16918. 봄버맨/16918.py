import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())
field = []
boomList = deque()

#상하좌우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(R):
    row = list(sys.stdin.readline().strip())
    field.append(row)
    
    for j in range(C):
        if(row[j] == 'O'):
            boomList.append([i, j]) 
            

# N이 0 이나 1 일 때 그대로 반환 
if(N<=1):
    for l in field:
        print(''.join(l))

# N이 2의 배수일 때 
#폭탄 설치
elif(N %2 ==0):
    for i in range(R):
        for j in range(C):
            if field[i][j] == '.':
                field[i][j]  = 'O'
    
    for l in field:
        print(''.join(l))
                

else:
    t = 1 #첫 1초는 아무것도 하지 않음
    while t<N:
        
        #폭탄 설치
        for i in range(R):
            for j in range(C):
                if field[i][j] == '.':
                    field[i][j]  = 'O'
        
        t+=1
        if(t==N):break        
                    
        #폭탄 터뜨리기
        #for boom in boomList:
        while boomList:
            x, y = boomList.popleft()
            field[x][y] ='.'
            for _ in range(4):
                nx = x+dx[_]
                ny = y+dy[_]
                
                if 0<=nx<R and 0<=ny<C:
                    field[nx][ny] = '.'
                #연쇄 반응 없음 
                    
        #남은 폭탄 저장            
        for i in range(R):
            for j in range(C):
                if field[i][j] == 'O':
                    boomList.append([i, j])
        
        t+=1
                    

    for l in field:
        print(''.join(l))