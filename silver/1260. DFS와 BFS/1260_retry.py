from collections import deque

N, M, V = list(map(int, input().split()))
graph = [ [] for _ in range(N+1)]
for i in range(M):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)

visited_1 = [0 for _ in range(N+1)]
visited_2 = [0 for _ in range(N+1)]

def dfs (startAt, graph, visited):
    visited[startAt] = 1
    graph[startAt].sort()
    curr_node = graph[startAt]

    print(startAt, end=' ')
    
    #print("curr_node", curr_node)
    
    for node in curr_node:
        if(visited[node]==0):
            dfs(node, graph, visited)
    
    
        
def bfs (startAt, graph, visited):
    queue = deque([startAt])
    
    while(queue):

        curr_node = queue.popleft()
        
       # print("graph[curr_node]", graph[curr_node])
        graph[curr_node].sort()
        curr_node_data = graph[curr_node]
    
        
        if(visited[curr_node]==0):
            visited[curr_node] =1
            print(curr_node, end=' ')
            
            for node in curr_node_data:
                queue.append(node)
        
       
            
        
    
dfs(V, graph, visited_1)
print()
bfs(V, graph, visited_2)