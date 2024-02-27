import sys

N = int(input())
A = list(map(int, input().split(" "))) #재배열가능
B = list(map(int, input().split(" "))) #재배열불가능

#A 재배열
A.sort(reverse=True)
#B 재배열
B.sort()

#어차피 구해야 하는 것은 합이므로 
# 정렬을 통해 큰값X작은값 순으로 곱하여 더하면 그것이 최소(집합과 그 합인)값이 된다. 
ans = 0
for i in range(N):
    ans+=A[i]*B[i]
    
print(ans)