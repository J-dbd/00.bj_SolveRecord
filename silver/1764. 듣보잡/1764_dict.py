# 틀림
import sys

N, M = map(int, sys.stdin.readline().strip().split(" "))

not_listen = dict()

not_listen_and_seen =[]
ans_num = 0
for _ in range(N): 
    name = sys.stdin.readline().strip()
    not_listen[name] = 1
for _ in range(M):
    name = sys.stdin.readline().strip()
    if(name in not_listen):
        not_listen_and_seen.append(name)
        ans_num+=1

ans = sorted(not_listen_and_seen)

print(ans_num)
for name in ans:
    print(name)