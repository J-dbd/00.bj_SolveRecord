import sys

T = int(input())



def dfs(curr, arr, visited):
    visited[curr] = 1
    next = arr[curr]
    
    if(visited[next] ==1):
        return
    
    dfs(next, arr, visited)
    
    
    
    
    
for _ in range(T):
    cnt = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    visited = [0] * (cnt+1)
    ans = 0
     
    arr.insert(0, 0)
    
    for i in range(1, cnt+1):
        if(visited[i]==0):
            dfs(i, arr, visited)
            ans+=1
    
    print(ans)
        

