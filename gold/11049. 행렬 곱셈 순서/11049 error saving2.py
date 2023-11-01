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
    mini=sys.maxsize # INF
    for k in range(i, j):
        #temp=c[i][k]+c[k+1][k]+(d[i-1]*d[k]*d[j])
        temp=c[i][k]+c[k+1][k]+(d[i]*d[k+1]*d[j+1])
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
    [0, 90, 60], 
    [0, 0, 30], 
    [0, 0, 0]]