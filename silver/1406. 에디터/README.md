# 첫 시도: Timeout

처음에 stack, list로 구현했는데 시간 초과가 떴다. python의 list는 연속된 메모리 공간을 차지하므로 해당 자료구조에서 삽입/삭제가 일어날 때 넣거나 뺀 곳의 자리를 뒤로 밀어두고 공간을 새로 생성하거나 다시 앞으로 땡겨야 하기 때문이다. 찾을 땐 O(1) 이지만 삽입/삭제시 그만큼의 연산이 더 일어나기 때문에 O(n)만큼 시간을 소요하니 당연히 time out이 뜬다. 길이나 문자열 명령어 개수를 볼 때 특히나 더 그렇다.

# 정리

[전략](https://www.acmicpc.net/board/view/54572)

1. list 의 맨 뒤에서만 삽입/삭제 연산을 할 수 있도록 알고리즘을 구현하기: 그렇게 함으로써 O(n)시간소요를 줄일 수 있다!

2. 한가운데의 원소를 삽입하거나 삭제했을 때 바로 앞뒤의 원소 이외의 원소를 건드릴 필요가 없는 자료구조를 사용하기

1번 전략은 stack을 두 개 사용하는 방법이고 2번은 연결리스트를 사용하는 방법이다.

# 2번 전략

양방향 연결 리스트를 사용하여 커서를 구현함으로서 해결한다.

## `cursor`개념

입력된 텍스트의 위치를 나타내며, 항상 어떤 문자의 왼쪽에 위치함을 기억해야 한다. 이 개념으로부터 `c.prev.data!=Node`을 통해 텍스트의 시작/끝에 위치하는지 아닌지를 판별할 수 있게 된다.

또한 조건문으로 커서의 위치 범위를 검사하고 적절한 동작을 수행함으로써 지속적으로 위치를 업데이트시킨다!

```python
L = DoublyLinkedList()
cursor = Node('|')

cursor.next = L.head
cursor.prev = L.head
L.head.next = cursor
L.head.prev = cursor
```

일단 여기서 시작점을 세팅 해두고,

```python
#set data
for t in text:
    #print("t in text", t)
    L.insertBefore(cursor, t)
```

이곳에서 cursor의 앞에 text를 삽입할 때 cursor도 함께 넣어주면,

```python

    def splice(self, x, y, given):

        if x==None or y==None or given==None: return
        # 1. x, y 를 특정지어 전달하면 해당 구간을 자른다.
        x.prev.next = y.next
        y.next.prev = x.prev

        # 2. 잘라낸[x, y]를 given 다음에 삽입하기?
        given.next.prev = y
        y.next = given.next
        x.prev = given
        given.next = x

    def moveAfter(self, x, given):
        self.splice(x, x, given)

    def moveBefore(self, x, given):
        self.splice(x, x, given.prev)

    def insertBefore(self, a, data):
        self.moveBefore(Node(data), a)
```

insertBefore->moveBefore->splice로 가서 cursor와 연결지으며 생성한다. 이 과정이 처음엔 꽤 복잡해보이는데 조금 생각하면 이해가 된다. 다만 아직 익숙치 않아서 많이 구현 연습을 해보아야겠다.

- 코드 출처: [링크](https://velog.io/@crookid/1406)
- 연결리스트 관련 공부 자료(youtube [링크](https://www.youtube.com/watch?v=K1PlysPgNZY))
