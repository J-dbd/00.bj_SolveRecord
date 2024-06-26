# DP vs BFS/DFS 알아보기

이번 문제의 경우 경로 이동이 x,y 모두 전진 밖에 없다. 따라서 모든 방문 경로가 최단거리임이 보증된다. (중요) DFS를 사용하지 않아도, 이전에 다녀온 경로에서의 경우의 수를 더해 다음 경로까지의 경로의 수를 구할 수 있으므로 DP를 사용한다. 또한 이번 문제에서는 어떤 노드를 기준으로 도착한 경로들의 갯수를 새야 했다.

    # arr[y][x]가 될 것
    # 오른쪽으로만 갈 수 있다: 가리키고 있는 인덱스 값이 증가한다.
    # 아래로만 갈 수 있다: 가리키고 있는 인덱스 값이 증가한다

# graph 섞인 DP : n+1, m+1

- 초기화를 잘 하자. 이번 문제의 경우 0으로 해 두었다.
- 특히 x, y 식 좌표 움직임이 필요할 때, n+1, m+1을 통해 range(1,n+1) 식으로 관리하는 것이 코드 이해나 구현에 더 용이한 것 같다. 그리고 indexError를 방지할 수 있다.
- 반복문으로 이동할 때, 0이 되지 않도록 체크해두는 것도 중요하다.
