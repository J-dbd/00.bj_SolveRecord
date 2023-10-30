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

# string_a = ' ' + sys.stdin.readline().rstrip()
# string_b = ' ' + sys.stdin.readline().rstrip()
# print(len(string_a), len(string_b))
# dp = [[0] * len(string_b) for _ in range(len(string_a))]

# for i in range(1, len(string_a)):
#     for j in range(1, len(string_b)):
#         if string_a[i] == string_b[j]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
# print(dp)