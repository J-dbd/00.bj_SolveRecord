import sys
from collections import deque
V, E = list(map(int, sys.stdin.readline().strip().split()))

#데이터 입력 받을 세팅
graph=[[] for _ in range(V+1)]
indegree=[0]*(V+1)

#간선 수에 따라 데이터 입력
# indegree 테이블에 값 넣어두기
for _ in range(E):
    sp, ep=list(map(int, sys.stdin.readline().strip().split()))
    graph[sp].append(ep)
    indegree[ep]+=1
    

def topo_sort(graph, indegree):
    # 1. 큐 세팅
    q=deque()
    res=[]
    
    #2. 큐에 진입 차수가 0인 노드를 입력 
    for i in range(1, V+1):
        if indegree[i]==0:
            q.append(i)
    
    # 3. 큐가 존재하는 동안 반복 시작
    while q:
        # 4. 현재 다루는 vertex 꺼냄
        now=q.popleft()
        res.append(now)
        
        # 5. 현재 다루는 vertex index에 저장된 vertex는 도착점이고 
        # 간선을 지워 indegree를 하나씩 내린다. 
        # 총 횟수는 그래프의 vertex 수만큼만 반복한다.
        for v in graph[now]:
            indegree[v]-=1
            #내리다 보면 0 이 되는데, 그렇다면 큐에 넣어둔다. 
            if indegree[v]==0:
                q.append(v)
        
    return res

answer=topo_sort(graph, indegree)
print(*answer, sep=' ')