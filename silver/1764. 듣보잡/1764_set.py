
import sys

N, M = map(int, sys.stdin.readline().strip().split(" "))

not_listen = set()
not_seen = set()
for _ in range(N): 
    temp = sys.stdin.readline().strip()
    not_listen.add(temp)

for _ in range(M):
    temp = sys.stdin.readline().strip()
    not_seen.add(temp)

not_listen_and_seen = not_seen & not_listen
ans = sorted(not_listen_and_seen)

print(len(ans))
for p in ans:
    print(p)