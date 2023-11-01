import sys
N= int(input())

data=[]

for _ in range(N):
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    if _ ==0:
        data.append(a)
    data.append(b)


c = [[0 for _ in range(N+1)]  for _ in range(N+1)]


def minimim(d, c, i, j):
    mini=sys.maxsize
    for k in range(i, j):
        temp=c[i][k]+c[k+1][j]+(d[i-1]*d[k]*d[j])
        if temp<mini:
            mini=temp
    return mini

#diagnoal
n=len(data)-1
for diagonal in range(1, n):
    for i in range(1, n-diagonal+1):
        j=i+diagonal
        if j+1 == i:
            c[i][j]=0
        c[i][j]=minimim(data, c, i, j) 


    



print(c[1][-1])


# nn=len(data)
# for i in range(1,nn):
#     for d in range(1,nn-i+1):
#         j=d+i
#         if i==j:
#             c[i][j]=0
#         if j>N:
#             continue
#         if i<j:
#             c[i][j]=minimim(data,c,i,j)
            
# for i in range(1,N+1):
#     for j in range(1, N+1):
#         if i==j:
#             c[i][j]=0
#         if i<j:
#             c[i][j]=minimim(d,c,i,j)




[
    [0, 0, 0, 0, 0], 
    [0, 0,60,40,20], 
    [0, 0, 0,24,12], 
    [0, 0, 0, 0, 6], 
    [0, 0, 0, 0, 0]]

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


[
    #[0, 0, 0, 0, 0, 0], 
    [0, 0, 105, 240, 270, 70], 
    [0, 0, 0, 189, 231, 42], 
    [0, 0, 0, 0, 297, 54], 
    [0, 0, 0, 0, 0, 198], 
    [0, 0, 0, 0, 0, 0]]


[
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 105, 240, 270, 70], 
    [0, 0, 0, 189, 231, 42], 
    [0, 0, 0, 0, 297, 54], 
    [0, 0, 0, 0, 0, 198], 
    [0, 0, 0, 0, 0, 0]
    ]


[
    [0, 0, 0, 0, 0], 
    [0, 0, 24, 28, 58], 
    [0, 0, 0, 16, 36], 
    [0, 0, 0, 0, 40], 
    [0, 0, 0, 0, 0]]