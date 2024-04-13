import sys
sys.setrecursionlimit(10**6)


T = int(input())

def bfs1(curr, graph, visited, res):
    if(graph[curr]==[]): 
        return 0
    
    next = graph[curr].pop()
    
    if(next == curr):
        return 1
        
    
    if(visited[next]==1): #완결해야 하는 부분
        res+=1
        return res

    if(visited[next]==0):
        visited[next]=1
        return bfs1(next, graph, visited, res)

def bfs2(curr, graph, visited):
    visited[curr]=1
    
    #print("curr", curr, "/visited", visited)
    
    if(graph[curr]==[]):
        return
    
    next = graph[curr].pop()
    
    if(visited[next]==0):
        bfs2(next, graph, visited)
    
    return
        
    

def find_graph(cnt, arr1, arr2):

    ans = 0
    graph =[[] for _ in range(cnt+1)]
    visited = [0]*(cnt+1)
    for i in range(cnt):
        x, y = arr1[i], arr2[i]
        graph[x].append(y)
        
    #print("g", graph)
        
    for i in range(1,cnt+1):
        if(visited[i]==0):
            bfs2(i, graph, visited)
            ans+=1
        
    return ans
        
        
    
    

for _ in range(T):
    cnt_nodes = int(input())
    
    first_line = list(range(1, cnt_nodes+1))
    second_line = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    print(find_graph(cnt_nodes, first_line, second_line))
