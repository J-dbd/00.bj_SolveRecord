N, M, V = list(map(int, input().split()))
graph = [ [] for _ in range(N+1)]
for i in range(M):
    s, e = list(map(int, input().split()))
    graph[s].append([s, e])
    graph[e].append([e, s])
    
print(graph)

visited = [0 for _ in range(N+1)]