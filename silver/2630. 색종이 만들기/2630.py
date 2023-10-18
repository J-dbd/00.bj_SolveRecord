import sys
N=int(input())
data=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white, blue = 0, 0

def cut(x,y,n):
    #기준점이 되는 색을 저장 
    color=data[x][y]
    global white, blue
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color!=data[i][j]:
                cut(x,y, n//2)
                cut(x+n//2, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y+n//2, n//2)
                return 
            
    if color==0:
        white+=1
    elif color==1:
        blue+=1

cut(0,0,N)
print(white)
print(blue)
            
    
    