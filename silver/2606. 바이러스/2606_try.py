
import sys 
from collections import deque
V=int(input())
E=int(input())

graph=[[] for _ in range(V+1)]

for _ in range(E):
    sp, ep = list(map(int, sys.stdin.readline().strip().split()))
    graph[sp].append(ep)
    graph[ep].append(sp)
    
queue=deque(graph[1])
visited=set()
visited.add(1)
while queue:
    #print("q", queue)
    now=queue.popleft()
    visited.add(now)
    
    for v in graph[now]:
        if v not in visited:
            visited.add(v)
            queue.append(v)

print(len(visited)-1)
    
############# 크루스칼 트라이 기록
# 유니온파인드 
# 를 어디에 썼더라? 
# 최소신장트리에서 
# 최소신장트리 - 크루스칼 로 했던 거 같음 
# 크루스칼이...... 최단거들을 연결하는 거였는데 
# 이거 응용하는 거 같은데...


# edges=[] #크루스칼은 간선을 받는다!
# result=0

# for _ in range(E):
#     start, end = list(map(int, sys.stdin.readline().strip().split()))
#     edges.append(start, end)

# parent=[0]*(V+1)

# #parent세팅 
# for i in range(V+1):
#     parent[i]=i
    


# def find_parent(parent, v):
#     if parent[v]!=v:#자기자신이 부모노드가 아니라면 
#         parent[v]=find_parent(parent, v)
    
#     return parent[v]

# def union(parent, a, b):
#     parent_of_a=find_parent(parent, a)
#     parent_of_b=find_parent(parent, b)
    
#     if parent_of_a<parent_of_b:
#         parent[b]=parent_of_a
#     else:
#         parent[a]=parent_of_b
        


# for edge in edges:
#     start, end=edge
#     if find_parent(parent, start) != find_parent(parent, end):
#         continue
    