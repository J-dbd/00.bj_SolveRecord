'''
메모리 초과!
'''
import sys

V, E, K, start_point = list(map(int, sys.stdin.readline().strip().split()))

INF=sys.maxsize

graph=[[INF]*(V+1) for _ in range(V+1)]


for i in range(E):
    s, e=list(map(int, sys.stdin.readline().strip().split()))
    graph[s][e]=1
    

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])


                

# 그래프 인쇄(1부터 시작!)
# for i in range(1, V+1):
#     for j in range(1, V+1):
#         if graph[i][j]==INF:
#             print("-", end=' ')
#         else:
#             print(graph[i][j], end=' ')
#     print()
    

def searching(graph, start_point):
    res=[]
    for j in range(1, V+1):
        if graph[start_point][j]==K:
            res.append(j)
    # for i in range(1, V+1):
    #     for j in range(1, V+1):
    #         if graph[i][j]==K:
    #             res.append(j)
    
    if res==[]:
        return [-1]
    else:
        return res                    
print(*searching(graph, start_point), sep='\n')
    
