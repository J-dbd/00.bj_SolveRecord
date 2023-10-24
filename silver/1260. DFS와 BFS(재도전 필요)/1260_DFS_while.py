import sys
from collections import deque
V, E, n= list(map(int,sys.stdin.readline().strip().split()))

#init graph
#graph={i:[] for i in range(0, V+1)}
graph=[]
[graph.append([]) for _ in range(0, V+1)]

#set graph
for i in range(1,E+1):
    start, end=list(map(int,sys.stdin.readline().strip().split()))
    graph[start].append(end)#indirected graph
    graph[end].append(start)

#print(graph)

#[[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
def DFS(graph, start):
    stack=[]
    seen=set()
    stack.append(start)
    #seen.add(start)
    

    while stack:
        print("stack?",stack)
        current_v=stack.pop()
        possible_v=sorted(graph[current_v], reverse=True)
        
        
        # for v in possible_v:
        #     if v not in seen:
        #         stack.append(v)
        #         seen.add(v)
        
        if current_v not in seen:
            seen.add(current_v)
            stack.extend(possible_v)
            
            
    return seen

def iterDFS(rooms, start) -> bool:
    seen = set()
    stack = []
    res=[]    
    stack.append(start)
    seen.add(start)
    #print(0, end=' ')
    res.append(start)
    

    while stack:
        room_idx = stack.pop()
        keys = rooms[room_idx]
        
        res.append(room_idx)
        for key in keys:
            if key not in seen:
                stack.append(key)
                seen.add(key)
                print(key, end=' ')
        
    if len(rooms) == len(seen):
        return res  
    else:
        return False
    
    
def BFS(graph, start):
    queue=deque()
    seen=set()
    res=[]
    
    queue.append(start)
    seen.add(start)
    
    while queue:
        current_v=queue.popleft()
        possible_v=sorted(graph[current_v])
        #print("possible_v",possible_v)
        res.append(current_v)
        
        for v in possible_v:
            if v not in seen:
                queue.append(v)
                seen.add(v)
    
    if len(graph)-1==len(seen):
        return res
    else: return res
    
visited_dfs=[False]*len(graph)

def dfs(v):
    visited_dfs[v]
    print(v, end=' ')
    
    for i in range(1, V-1):
        if visited_dfs[i]==False:
            dfs(i)
#[[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
def DFS_main(graph, v):
    visited=set()
    visited.add(v)
    res=[]
    res.append(v)
    
    def DFS(v):
        #print("V in DFS",v)
        
        #print(v, end=' ')
        #res.append(v)
        for v in sorted(graph[v]):
            if v not in visited:
                visited.add(v)
                #print("!!!!",v, end=' ')
                res.append(v)
                DFS(v)
    
    for i in range(1, V+1):
        DFS(i)
    
    return res
     


 
#print(graph)   


print("anser")
#DFS_main(graph, n)
print(DFS_main(graph, n))
#print(dfs(n))
#print(iterDFS(graph,n))
print(BFS(graph,n))


