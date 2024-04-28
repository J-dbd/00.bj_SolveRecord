def solution(m, n, puddles):
    div= 1000000007
    answer = 0
    x, y = m, n
    
    graph = [[0]*(x+1) for _ in range(y+1)]
    graph[1][1] = 1
    
    # for pd in puddles:
    #     x, y = pd
    #     graph[y][x] = 0

    #arr[y][x]가 될 것
    # 오른쪽으로만 갈 수 있다: 가리키고 있는 인덱스 값이 증가한다.
    # 아래로만 갈 수 있다: 가리키고 있는 인덱스 값이 증가한다
    
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(i==1 and j ==1): continue
            if([j, i] in puddles):continue

            graph[i][j] = (graph[i-1][j] + graph[i][j-1]) % div
            
    #print(graph)
    answer = graph[n][m] 

    return answer