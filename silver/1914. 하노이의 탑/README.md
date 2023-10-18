[백준 문제 링크](https://www.acmicpc.net/problem/1914)

# 하노이의 탑 : 1914

재귀함수로 풀어야 하는 문제.

### 문제 풀이

#### 주요 문제 해결 방법: 재귀

main problem : n개의 원반을 이동하라

subproblem과 pattern:

1. n-1개의 원반을 목적지(end, destination)가 아닌 다른 곳(other)으로 이동하기.
2. 가장 큰 원반을 목적지에 이동하기.

```python
def hanoi(n, start, end, other):
    if n==0:
    return

    hanoi(n-1,start,other,end)
    print(start,end) #재귀적으로 호출될 때 end는 other로 받았다.
    hanoi(n-1,other,end,start)

```

#### 이동횟수 이슈

n번째 원반의 총 이동횟수를 일반화하면 a[n]번 이동한다. n번째 원반을 이동하려면 n-1번째 원반을 목적지가 아닌 다른 곳(other)에 이동하고, 큰 원반을 목적지로 이동하고, other에 이동된 n-1개의 원반을 다시 목적지에 이동해야 한다. 따라서 ...n개의 원반의 이동횟수는 다음과 같다.

```
a[n] =  a[n-1] + 1 + a[n-1]
a[n] = 2*a[n-1]+1
```

##### 점화식으로 값을 알아내는 방법

여기서 일반화 및 등비수열의 합 공식을 사용해 $2^{n-1}-1$이 최소이동횟수라고 알 수 있다.

$a_{n}=2a_{n-1}+1$

1. 양변에 1을 더한다.

$a_{n}+1=2a_{n-1}+2$

2. 우변을 2로 묶는다.

$a_{n}+1=2(a_{n-1}+1)$

3. $a_{n}+1$ 을 $b_{n}$으로 대입하여 생각

$b_{n}=2b_{n-1}$ : 공비가 2인 공비수열

4. 첫째항으로 밑 구하기

$a_{1}=1$ 이므로 $b_{1}=2$ <--- $b_{1}=a_{1}(=1)+1=2$

5. 따라서 $b_{n}$은 첫째항이 2, 공비가 2인 공비수열이 된다.

$b_{n}=a_{n}+1=2^{n-1}$

$a_{n}=2^{n-1}-1$

##### 참고 링크

[하노이의 탑 점화식과 일반항 증명](http://mathought.com/bbs/board.php?bo_table=04_5&wr_id=122&sfl=&stx=&sst=wr_datetime&sod=asc&sop=and&page=2)
[수열로 표현하기 이해 쉬운 자료](https://velog.io/@younghoondoodoom/%EB%B0%B1%EC%A4%80-11729-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9C)
