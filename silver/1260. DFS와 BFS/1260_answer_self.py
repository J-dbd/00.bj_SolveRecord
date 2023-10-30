import sys
V, E, start_point=list(map(int, sys.stdin.readline().strip().split()))

graph=[[] for _ in range(V+1)]

for _ in range(E):
    s, e = list(map(int, sys.stdin.readline().strip().split()))
    graph[s].append(e)
    graph[e].append(s)

def DFS(node):
    visited=[False]*(V+1)
    stack=[node]
    res=[]
    while stack:
        now=stack.pop()
        if not visited[now]:
            visited[now]=True
            stack.extend(sorted(graph[now], reverse=True))
            res.append(now)
    return res

from collections import deque
def BFS(node):
    queue=deque([node])
    res=[]
    visited=[False]*(V+1)
    while queue:
        #print(queue)
        now=queue.popleft()
        if not visited[now]:
            visited[now]=True
            queue.extend(sorted(graph[now]))
            res.append(now)
            
    return res

print(*DFS(start_point), sep=' ')
print(*BFS(start_point), sep=' ')
        
    
        
            