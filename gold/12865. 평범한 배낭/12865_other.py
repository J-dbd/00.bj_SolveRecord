import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
            
            
#냅색 문제 풀이
for i in range(1, K + 1):
    for j in range(1, N + 1):
        weight = stuff[j][0] 
        value = stuff[j][1]
       
        if i < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            #knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
            knapsack[i][j] = max(value + knapsack[i - weight][j - 1], knapsack[i][j-1])

#print(knapsack[N][K])

print(knapsack)

# https://gsmesie692.tistory.com/113