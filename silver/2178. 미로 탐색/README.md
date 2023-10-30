# 미로 탐색

유형: 좌표이동-미로탐색, 최단 경로

좌표를 따라 이동하는 유형의 문제.

이 문제는 최단 경로이므로 BFS를 사용해야 한다.

## 1. 이동을 어떻게 할 것인가?

이러한 문제는 변화량을 나타내는 dx, dy 형태로 문제에서 제시한 이동 가능한 움직임을 1차원 배열 형태로 만들고

현재 위치에서 동서남북을 탐색 후 이동 한다.

```python
# 위/아래/오른쪽/왼쪽
dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
```

## 2. 미로 내의 움직임 표현

특정 범위 내에서만 움직여야 하므로 무작정 움직일 수는 없다. 범위를 지정해 주어야 하는데 어떻게 할 것인가?

```python
# n, m = 필드의 너비와 높이
for i in range(4):
    next_x, next_y = x+dx[i], y+dy[i]
    if 0<= next_y < n and 0<= next_y < m: #다음 좌표가 범위를 벗어나는지 확인
        #벗어나지 않다면 여기서 무언가를 함
```

```
0번째 queue: deque([(0, 0)])
    next_x = 0 + 0 /     next_y = 0 + 1
        graph[0][1]=0
    next_x = 0 + 0 /     next_y = 0 + -1
    next_x = 0 + 1 /     next_y = 0 + 0
        graph[1][0]=1
    next_x = 0 + -1 /     next_y = 0 + 0
. . . . . . . . . . .
1번째 queue: deque([(1, 0)])
    next_x = 1 + 0 /     next_y = 0 + 1
        graph[1][1]=0
    next_x = 1 + 0 /     next_y = 0 + -1
    next_x = 1 + 1 /     next_y = 0 + 0
        graph[2][0]=1
    next_x = 1 + -1 /     next_y = 0 + 0
        graph[0][0]=1
. . . . . . . . . . .
2번째 queue: deque([(2, 0), (0, 0)])
    next_x = 2 + 0 /     next_y = 0 + 1
        graph[2][1]=0
    next_x = 2 + 0 /     next_y = 0 + -1
    next_x = 2 + 1 /     next_y = 0 + 0
        graph[3][0]=1
    next_x = 2 + -1 /     next_y = 0 + 0
        graph[1][0]=2
. . . . . . . . . . .
3번째 queue: deque([(0, 0), (3, 0)])
    next_x = 0 + 0 /     next_y = 0 + 1
        graph[0][1]=0
    next_x = 0 + 0 /     next_y = 0 + -1
    next_x = 0 + 1 /     next_y = 0 + 0
        graph[1][0]=2
    next_x = 0 + -1 /     next_y = 0 + 0
. . . . . . . . . . .
4번째 queue: deque([(3, 0)])
    next_x = 3 + 0 /     next_y = 0 + 1
        graph[3][1]=1
    next_x = 3 + 0 /     next_y = 0 + -1
    next_x = 3 + 1 /     next_y = 0 + 0
    next_x = 3 + -1 /     next_y = 0 + 0
        graph[2][0]=3
. . . . . . . . . . .
5번째 queue: deque([(3, 1)])
    next_x = 3 + 0 /     next_y = 1 + 1
        graph[3][2]=1
    next_x = 3 + 0 /     next_y = 1 + -1
        graph[3][0]=4
    next_x = 3 + 1 /     next_y = 1 + 0
    next_x = 3 + -1 /     next_y = 1 + 0
        graph[2][1]=0
. . . . . . . . . . .
6번째 queue: deque([(3, 2)])
    next_x = 3 + 0 /     next_y = 2 + 1
        graph[3][3]=0
    next_x = 3 + 0 /     next_y = 2 + -1
        graph[3][1]=5
    next_x = 3 + 1 /     next_y = 2 + 0
    next_x = 3 + -1 /     next_y = 2 + 0
        graph[2][2]=1
. . . . . . . . . . .
7번째 queue: deque([(2, 2)])
    next_x = 2 + 0 /     next_y = 2 + 1
        graph[2][3]=0
    next_x = 2 + 0 /     next_y = 2 + -1
        graph[2][1]=0
    next_x = 2 + 1 /     next_y = 2 + 0
        graph[3][2]=6
    next_x = 2 + -1 /     next_y = 2 + 0
        graph[1][2]=1
. . . . . . . . . . .
8번째 queue: deque([(1, 2)])
    next_x = 1 + 0 /     next_y = 2 + 1
        graph[1][3]=0
    next_x = 1 + 0 /     next_y = 2 + -1
        graph[1][1]=0
    next_x = 1 + 1 /     next_y = 2 + 0
        graph[2][2]=7
    next_x = 1 + -1 /     next_y = 2 + 0
        graph[0][2]=1
. . . . . . . . . . .
9번째 queue: deque([(0, 2)])
    next_x = 0 + 0 /     next_y = 2 + 1
        graph[0][3]=1
    next_x = 0 + 0 /     next_y = 2 + -1
        graph[0][1]=0
    next_x = 0 + 1 /     next_y = 2 + 0
        graph[1][2]=8
    next_x = 0 + -1 /     next_y = 2 + 0
. . . . . . . . . . .
10번째 queue: deque([(0, 3)])
    next_x = 0 + 0 /     next_y = 3 + 1
        graph[0][4]=1
    next_x = 0 + 0 /     next_y = 3 + -1
        graph[0][2]=9
    next_x = 0 + 1 /     next_y = 3 + 0
        graph[1][3]=0
    next_x = 0 + -1 /     next_y = 3 + 0
. . . . . . . . . . .
11번째 queue: deque([(0, 4)])
    next_x = 0 + 0 /     next_y = 4 + 1
        graph[0][5]=1
    next_x = 0 + 0 /     next_y = 4 + -1
        graph[0][3]=10
    next_x = 0 + 1 /     next_y = 4 + 0
        graph[1][4]=1
    next_x = 0 + -1 /     next_y = 4 + 0
. . . . . . . . . . .
12번째 queue: deque([(0, 5), (1, 4)])
    next_x = 0 + 0 /     next_y = 5 + 1
    next_x = 0 + 0 /     next_y = 5 + -1
        graph[0][4]=11
    next_x = 0 + 1 /     next_y = 5 + 0
        graph[1][5]=0
    next_x = 0 + -1 /     next_y = 5 + 0
. . . . . . . . . . .
13번째 queue: deque([(1, 4)])
    next_x = 1 + 0 /     next_y = 4 + 1
        graph[1][5]=0
    next_x = 1 + 0 /     next_y = 4 + -1
        graph[1][3]=0
    next_x = 1 + 1 /     next_y = 4 + 0
        graph[2][4]=1
    next_x = 1 + -1 /     next_y = 4 + 0
        graph[0][4]=11
. . . . . . . . . . .
14번째 queue: deque([(2, 4)])
    next_x = 2 + 0 /     next_y = 4 + 1
        graph[2][5]=1
    next_x = 2 + 0 /     next_y = 4 + -1
        graph[2][3]=0
    next_x = 2 + 1 /     next_y = 4 + 0
        graph[3][4]=1
    next_x = 2 + -1 /     next_y = 4 + 0
        graph[1][4]=12
. . . . . . . . . . .
15번째 queue: deque([(2, 5), (3, 4)])
    next_x = 2 + 0 /     next_y = 5 + 1
    next_x = 2 + 0 /     next_y = 5 + -1
        graph[2][4]=13
    next_x = 2 + 1 /     next_y = 5 + 0
        graph[3][5]=1
    next_x = 2 + -1 /     next_y = 5 + 0
        graph[1][5]=0
. . . . . . . . . . .
16번째 queue: deque([(3, 4), (3, 5)])
    next_x = 3 + 0 /     next_y = 4 + 1
        graph[3][5]=15
    next_x = 3 + 0 /     next_y = 4 + -1
        graph[3][3]=0
    next_x = 3 + 1 /     next_y = 4 + 0
    next_x = 3 + -1 /     next_y = 4 + 0
        graph[2][4]=13
. . . . . . . . . . .
17번째 queue: deque([(3, 5)])
    next_x = 3 + 0 /     next_y = 5 + 1
    next_x = 3 + 0 /     next_y = 5 + -1
        graph[3][4]=14
    next_x = 3 + 1 /     next_y = 5 + 0
    next_x = 3 + -1 /     next_y = 5 + 0
        graph[2][5]=14
. . . . . . . . . . .
15

```
