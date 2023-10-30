import sys
X, Y = [ sys.stdin.readline().strip() for _ in range(2)]

def LCS(X,Y):
    X, Y = ' '+X, ' '+Y # 편의를 위한 장치 
    m,n = len(X), len(Y)
    c=[[0 for _ in range(n)] for _ in range(m)] # Y, X
    
    
    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[j]:
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=max(c[i-1][j], c[i][j-1])
                
    
    return c[-1][-1] 

print(LCS(X,Y))

