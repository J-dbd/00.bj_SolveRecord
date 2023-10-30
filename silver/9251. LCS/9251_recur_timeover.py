import sys
X = input()
Y = input()

sys.setrecursionlimit(20000)

###### recursion ######
###### 시간 초과 ###### 

def LCS(X, Y):
    m = len(X)
    n = len(Y)

    if m ==0 or n ==0:
        return 0
    else:
        if X[-1]==Y[-1]:
            return LCS(X[:(m-1)], Y[:(n-1)])+1
        
        else:
            return max(
                LCS(X[:m-1], Y[:n]),
                LCS(X[:m], Y[:n-1])
            )
    
print(LCS(X, Y))