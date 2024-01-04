
import sys
n, k = list(map(int, sys.stdin.readline().split()))


dp = [0 for _ in range(k+1)]
dp[0] = 1


coins = [int(input()) for _ in range(n)]

for coin in coins:
    


    for j in range(coin, k+1): 
        if (j - coin) >= 0:
            dp[j] += dp[j-coin]
    
    
    # for printing ================================
    
    # for j in range(coin, k+1): 
    #     if (j - coin) >= 0:
    #         print(f'[{j}] :: dp[{j}] = {dp[j]} + dp[{j-coin}] = {dp[j-coin]}')
    #         dp[j] += dp[j-coin]
    #         print(f"dp/coin : {coin}: ", dp)
    
    # print("-----------")
    
    # for printing ================================
            
print(dp[k])        
