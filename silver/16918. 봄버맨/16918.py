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
            
         
#print(boomList)   
t = 1

if(N % 4 == 1): 
    t = 0
    
elif(N % 4 == 0):
    t = 0

while t<N:
    print("N: ", t)
    t +=1
    if(t==N): break
    
    # print(t, "초")
    
    #폭탄 설치
    for i in range(R):
        for j in range(C):
            if field[i][j] == '.':
                field[i][j]  = 'O'
                
    # print(f"{t} 초 : 모든 칸에 폭탄 설치(3)")
    # for l in field:
    #     print(''.join(l))           
    
    #폭탄 터뜨리기
    #for boom in boomList:
    while boomList:
        x, y = boomList.popleft()
        
        for _ in range(4):
            nx = x+dx[_]
            ny = y+dy[_]
            
            if 0<=nx<R and 0<=ny<C:
                field[nx][ny] = '.'
                
    # print(f"{t} 초 : 폭탄 폭발(4)")
    # for l in field:
    #     print(''.join(l))
                
    #남은 폭탄 저장            
    for i in range(R):
        for j in range(C):
            if field[i][j] == 'O':
                boomList.append([i, j])
                

print("--")
for l in field:
    print(''.join(l))