import sys
from collections import deque
V, E, K, start_point = list(map(int, sys.stdin.readline().strip().split()))

#2차원 리스트의 메모리 < 인접 행렬 메모리
graph=[[] for _ in range(V+1)]

#방문 체크용 및 거리 체크용 
#다익스트라/플-워의 개념을 차용
#음수로 기본 세팅 후 시작점만 0으로 치환
distance=[-1]*(V+1)
distance[start_point]=0

#정보 받음
for i in range(E):
    s, e=list(map(int, sys.stdin.readline().strip().split()))
    graph[s].append(e)

#최단 거리를 찾는 문제
#이동 값이 1이므로 BFS를 사용
def BFS(graph, start_point, distance):
    q=deque([start_point])
    
    while q:
        now=q.popleft()
        for next_v in graph[now]:
            # 방문 여부를 체크
            if distance[next_v]==-1:
                distance[next_v]=distance[now]+1 #지금 간 곳까지 더해 준다.
                q.append(next_v)
    return distance

def pt(distance):
    res=[]
    for i in range(V+1):
        if distance[i]==K: res.append(i)
    
    if res==[]: return [-1]
    else: return res
    

answer=pt(BFS(graph, start_point, distance))
print(*answer, sep='\n')


