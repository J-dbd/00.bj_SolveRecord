from collections import deque
import sys

queue=deque()
result=[]

n, k=list(map(int, sys.stdin.readline().split()))

#큐 만들기 
for i in range(1, n+1):queue.append(i)

#k=3일때 앞에서 첫번째와 두번째 것을 pop(left)한다. 
#그리고 그것을 뒤로 보내 더한다 (append)
while queue:
    for i in range(k-1):
        queue.append(queue.popleft()) 
    #그 뒤에 result에 현재 queue의 맨 앞의 값을 더함
    #지금 여기서는 3번쨰 값이 맨 첫번째 자리에 와 있다!
    result.append(str(queue.popleft()))
    
    #이 과정을 queue가 더 남아있지 않을 때까지 반복한다. 

#출력
answer=', '.join(result)
print(f'<{answer}>')