import sys
_input = sys.stdin.readline().strip()
N, K = list(map(int, _input.split()))

coins=[list(map(int, sys.stdin.readline().strip().split()))[0] for _ in range(N)]

#print(coins)
res=0
for coin in coins[::-1]:
    if coin>K: 
        continue
    elif coin<=K:
        temp=K//coin
        K=(K-(temp*coin))%coin
        res+=temp
        
        if K==0:
            break


print(res)