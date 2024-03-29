# 원리

```
0 : 그대로
1: 아무것도 안 함
2: 폭탄 설치
3: 0에 설치한 게 터짐
4: 폭탄 설치
5: 2에 설치한 게 터짐
6: 폭탄 설치
7: 3에 설치한 게 터짐

```

# 반복문 while / for

```
RuntimeError: deque mutated during iteration
```

```python
#폭탄 터뜨리기
        #for boom in boomList:
        while boomList:
            x, y = boomList.popleft()
            field[x][y] ='.'
            for _ in range(4):
                nx = x+dx[_]
                ny = y+dy[_]

                if 0<=nx<R and 0<=ny<C:
                    field[nx][ny] = '.'
                #연쇄 반응 없음
```

이 코드에서 while 에서 deque를 사용한 boomList의 반복을 처음에 for문으로 하려고 했는데, while로 해야 한다.

## while

- 반복 시 조건의 참/거짓 여부반 확인

## for

- 반복 중인 객체(반복가능한)의 처음부터 끝까지를 순회한다.
- 따라서 그 구성/크기가 바뀌면 오류가 발생함. (바로 이번 경우)
