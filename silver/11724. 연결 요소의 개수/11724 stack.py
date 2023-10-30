import sys 
V, E= list(map(int, sys.stdin.readline().strip().split()))


graph=[[] for _ in range(V+1)]

for i in range(E):
    s, e =list(map(int, sys.stdin.readline().strip().split()))
    graph[s].append(e)
    graph[e].append(s)
    
stack=[]
visited=[False]*(V+1)
cnt=0

def DFS_stack(v, stack, visited):
    stack.append(v)
    visited[v]=True
    
    while stack:
        now=stack.pop()
        
        for vtx in graph[now]:
            if not visited[vtx]:
                stack.append(vtx)
                visited[vtx]=True
    

for i in range(1, V+1):
    if not visited[i]:
        DFS_stack(i, stack, visited)
        cnt+=1

print(cnt)