from collections import deque
N, L = map(int,(input().split()))
frts_origin = list(map(int, input().split()))
frts = sorted(frts_origin)

#큐로 작은 것부터 넣어 선입선출 하며 그때그때 확인후 먹는다.
eatable =deque()

L_eating = L
for f in frts:
    eatable.append(f)

while eatable:
    f = eatable.popleft()
    if(L_eating>=f): L_eating+=1
    else: continue



print(L_eating)


