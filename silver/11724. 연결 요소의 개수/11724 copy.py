import sys 
from collections import deque
V, E= list(map(int, sys.stdin.readline().strip().split()))

graph=[[] for _ in range(V+1)]

for i in range(E):
    s, e =list(map(int, sys.stdin.readline().strip().split()))
    graph[s].append(e)
    graph[e].append(s)

visited=[0]*(V+1)
cnt=0

def DFS(v):
    if visited[v]==1: 
        return v
    
    visited[v]=1
    #print(v, end=' ')
    
    for now in graph[v]:
        DFS(now)
        
for i in range(1, V+1):
    #print(f"----{i}번째 시작-----")
    #DFS(i)
    #print(DFS(i))

    if DFS(i)==None:
        cnt+=1
    #print("------{i}번째 종료----")
    
print(cnt)