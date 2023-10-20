import sys
T1=int(input())
#T1_arr=list(map(int, sys.stdin.readline().split()))
T1_arr=sys.stdin.readline().split()
T2=int(input())
#T2_arr=list(map(int, sys.stdin.readline().split()))
T2_arr=sys.stdin.readline().split()

for num in T2_arr:
    if num in T1_arr:
        print(1)
    else:
        print(0)

# list의 in은 시간복잡도 O(n)