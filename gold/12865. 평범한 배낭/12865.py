import sys
N, K = list(map(int, sys.stdin.readline().strip().split()))
#data setting
data_list=[[]] # 어떤 아이템도 선택하지 않은 경우를 위해 추가함
for i in range(N): 
    W, V  = list(map(int, sys.stdin.readline().strip().split()))
    data_list.append([W,V])

#작은 것부터 넣어보려고 추가.
data_list=sorted(data_list)

# dp 테이블 작성
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(K+1):
    for j in range(N+1):
        # 현재 생각중인 금액(i)가 0일 때  / 아무것도 선택하지 않았을 때 0 설정
        if i == 0 or j ==0 :
            dp[i][j]=0

        else:
            w, v = data_list[j]
            if i>=w:
                dp[i][j]=max(dp[i-w][j-1]+v, dp[i][j-1])
            
            else:
                dp[i][j]=dp[i][j-1]
                


print(dp[-1][-1]) 
        
