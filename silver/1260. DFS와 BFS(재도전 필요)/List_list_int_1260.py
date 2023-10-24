import sys
from collections import deque
V, E, n= list(map(int,sys.stdin.readline().strip().split()))

graph=[]
[graph.append([]) for _ in range(0, V+1)]


#set graph
for i in range(1,E+1):
    start, end=list(map(int,sys.stdin.readline().strip().split()))
    graph[start].append(end)#indirected graph
    graph[end].append(start)
    

def BFS(graph, start):
    queue=deque()
    seen=set()
    res=[]
    
    queue.append(start)
    seen.add(start)
    
    while queue:
        current_v=queue.popleft()
        possible_v=sorted(graph[current_v])
        res.append(current_v)
        
        for v in possible_v:
            if v not in seen:
                queue.append(v)
                seen.add(v)
    
    if len(graph)-1==len(seen):
        return res
    else: return res

def DFS_main(graph, v):
    visited=set()
    visited.add(v)
    res=[]
    res.append(v)
    
    def DFS(v):
        for vertex in sorted(graph[v]):
            if vertex not in visited:
                visited.add(vertex)
                res.append(vertex)
                DFS(vertex)
    
    for i in range(1, V+1):
        DFS(i)
    
    return res

dfs_result=DFS_main(graph, n)
bfs_result=BFS(graph,n)

print(*dfs_result, sep=' ')
print(*bfs_result, sep=' ')