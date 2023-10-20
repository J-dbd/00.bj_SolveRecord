import sys
n=int(input())
#N=set(map(int, sys.stdin.readline().split()))
N=set(sys.stdin.readline().split())
m=int(input())
M=sys.stdin.readline().split()
#M=list(map(int, sys.stdin.readline().split()))
#set활용
#arr=set(T1)
for m in M:
    print(1) if m in N else print(0)