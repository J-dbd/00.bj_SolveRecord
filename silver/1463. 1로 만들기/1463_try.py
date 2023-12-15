# x = int(input())

# dp = [0] * (1000001)

# for i in range(2, x+1):
#     dp[i] = dp[1-1] + 1
    
#     if(i%2 == 0):
#         dp[i] = min(dp[i//2]+1, dp[i])
    
#     if(i%3 ==0):
#         dp[i] = min(dp[i//3]+1, dp[i])

# print(dp[x])





# def calc_x(x, cnt):
#     if(x ==1):
#         return cnt
#     elif(x%2==0):
#         cnt+=1
#         return calc_x(x//2, cnt)
#     elif((x%3==0) and (x%2==1)):
#         cnt+=1
#         return calc_x(x//3, cnt)
#     else:
#         cnt+1
#         return calc_x(x-1, cnt)
# cnt = 0    
# ans = calc_x(x, cnt)
# print(ans)

