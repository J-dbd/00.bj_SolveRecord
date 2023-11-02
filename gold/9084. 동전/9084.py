import sys 

T= int(input())
data=[]
temp_dict={}
for i in range(T):
    N=int(input()) # 동전의 가짓수 
    coins=list(map(int, sys.stdin.readline().strip().split()))    #동전 금액 
    money=int(input()) #금액
    
    #dp 테이블
    #만들 수 있는 조합의 개수를 새야 함
    dp=[0 for _ in range(money+1)] #money 까지 가야 하므로..
    dp[0]=1
    
    #입력받은 동전들로 돌린다.
    for coin in coins:
        for i in range(money+1):
            # 현재 금액(i)를 현재 돌리고 있는 coin이 채울 수 있다면 
            # 이전까지의 경우의 수에 현재 동전으로 만들 수 있는 경우의 수를 더한다.
            # dp[i-coin]             dp[i]
            if i>=coin:
                dp[i]+=dp[i-coin]
                
    print(dp[money])  
    
    

