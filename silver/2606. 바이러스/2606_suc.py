
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
    