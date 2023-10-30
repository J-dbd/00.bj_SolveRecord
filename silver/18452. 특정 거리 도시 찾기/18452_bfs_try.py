import sys
from collections import deque
V, E, K, start_point = list(map(int, sys.stdin.readline().strip().split()))

graph=[[] for _ in range(V+1)]


for i in range(E):
    s, e=list(map(int, sys.stdin.readline().strip().split()))
    graph[s].append(e)
    
    
def BFS(graph, start_point):
    q=deque()
    seen=set()
    visited=[0]*(V+1)
    res=[]
    
    q.append(start_point)
    seen.add(start_point)
    visited[start_point]+=1
    
    while q:
        now=q.popleft()
        for v in graph[now]:
            if v not in seen:
                q.appendleft(v)
                seen.add(v)
                visited[v]+=1
        res.append(now)
        
    return res

print(BFS(graph, start_point))


