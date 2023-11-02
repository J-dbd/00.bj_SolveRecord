import sys
N= int(input())

d=[]

for _ in range(N):
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    if _ ==0:
        d.append(a)
    d.append(b)


c = [[0 for _ in range(N)]  for _ in range(N)]


def minimum(c, d, i, j):
    mini=sys.maxsize
    for k in range(i, j):
        temp=c[i][k]+c[k+1][j]+(d[i]*d[k+1]*d[j+1])
        print(temp, ':', i, j, k)
        if mini>temp:
            mini=temp
    
    return mini

for i in range(N):
    for j in range(N):
        if i==j:
            c[i][j]=0
        if i<j:
            c[i][j]=minimum(c, d, i, j)


print(c)


[
    [0, 0, 0, 0], 
    [0, 0, 30, 90], 
    [0, 0, 0, 36], 
    [0, 0, 0, 0]]


[
    [0, 0, 0, 0, 0], 
    [0, 0, 24, 12, 30], 
    [0, 0, 0, 16, 36], 
    [0, 0, 0, 0, 40], 
    [0, 0, 0, 0, 0]
    
    ]

[
    [0, 0, 0, 0, 0], 
    [0, 0, 24, 12, 30], 
    [0, 0, 0, 16, 36], 
    [0, 0, 0, 0, 40], 
    [0, 0, 0, 0, 0]]


    
