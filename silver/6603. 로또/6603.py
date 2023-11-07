import sys

def lotto(k, arr):
    visited = [0 for i in range(len(arr))]
    def dfs(starting, cnt):
        if(cnt==k):
            for i in range(len(arr)):
                if(visited[i]):
                    print(arr[i], end=' ')
            
            print()
            return
        
        for i in range(starting, len(arr)):
            if not visited[i]:
                visited[i] = 1
                dfs(i, cnt+1)
                visited[i] = 0
                
    
    dfs(0, 0)
    
def dfs_combo(cnt, arr, path):
    if(cnt==0):
        print(*path)
        return
    
    for i in range(len(arr)-cnt+1):
        path.append(arr[i])
        dfs_combo(cnt-1, arr[i+1:], path)
        path.pop()
    
    
num_list = []
while True:
    temp = list(map(int, sys.stdin.readline().split()))
    if(temp[0]==0): break
    k = temp[0]
    arr = temp[1:]
    
    visited = [0 for i in range(len(arr))]
    #lotto(6, arr)
    path=[]
    dfs_combo(6, arr,path)
    print()
