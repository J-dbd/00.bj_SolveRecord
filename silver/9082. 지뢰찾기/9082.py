import sys

T = int(input())

for _ in range(T):
    N = int(input())
    numline = list(map(int,(sys.stdin.readline().strip())))
    caseline = list(sys.stdin.readline().strip())
    
    templine = [0]*(N+1)
    
    print(templine)
    
    for i in range(N):
        if(i==0):
            templine[i]+=1
            templine[i+1]+=1
        
        else:
            templine[i-1]+=1
            templine[i]+=1
            templine[i+1]
            
        
        
            
            
    print(numline, caseline)
    
    print('templine', templine)
            
            
            