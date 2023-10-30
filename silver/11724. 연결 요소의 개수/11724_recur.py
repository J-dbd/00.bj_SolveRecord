import sys 
V, E= list(map(int, sys.stdin.readline().strip().split()))
#런타임 에러 : 재귀 제한 풀기
limit_number = 15000
sys.setrecursionlimit(limit_number)

graph=[[] for _ in range(V+1)]

for i in range(E):
    s, e =list(map(int, sys.stdin.readline().strip().split()))
    graph[s].append(e)
    graph[e].append(s)

visited=[False]*(V+1)
cnt=0

def DFS(v):
    visited[v]=1
    
    for now in graph[v]:
        if not visited[now]:
            DFS(now)
        
for i in range(1, V+1):
    if not visited[i]:
        DFS(i)
        cnt+=1
    
print(cnt)