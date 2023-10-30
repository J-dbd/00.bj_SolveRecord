import sys
from collections import deque
V, E, n= list(map(int,sys.stdin.readline().strip().split()))

#init graph
graph=[[0]*(V+1) for _ in range(0, V+1)]

#set graph
for i in range(E):
    start, end=list(map(int,sys.stdin.readline().strip().split()))
    graph[start][end]=1 #indirected graph
    graph[end][start]=1


def DFS(graph, start):
    stack=[]
    seen=set()
    res=[]
    stack.append(start)
    seen.add(start)
    seen.add(0)
    #res.append(start)
    while stack:
        current_v=stack.pop()
        #print("===")
        #print("current_v", current_v)
        possible_vs=graph[current_v]
        res.append(current_v)
        #print(current_v, end=' ')
        for i in range(len(possible_vs)-1, 0, -1):
            #print("possible_vs", possible_vs)
            #print(f'i:{i}/possible_vs[i]==1:{possible_vs[i]==1}/i not in seen:{i not in seen}')
            #print("seen",seen)
            if (possible_vs[i]==1) and (i not in seen):
                #print("i",i, end=' ')
                stack.append(i)
                seen.add(i)
        #print("----")
    
    return res

    
print("anser")
print(DFS(graph,n))



    
print("anser")
print(DFS(graph,n))
