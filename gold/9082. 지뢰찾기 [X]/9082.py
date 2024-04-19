import sys

T = int(input())

for _ in range(T):
    N = int(input())
    numline = list(map(int,(sys.stdin.readline().strip())))
    caseline = list(sys.stdin.readline().strip())
    
    #print(numline, caseline)
    numline.insert(0,0)
    numline.append(0)
    
    caseline.insert(0,"#")
    caseline.append("#")
    
    res = 0
    solid = 0
    
    for i in range(1, N+1):
        if(caseline[i]=='*'):
            numline[i-1]-=1
            numline[i]-=1
            numline[i+1]-=1
            solid+=1
 
    
    for i in range(1, N+1):
        

        
        if(numline[i]==0) and (numline[i+1]==0): 
            res+=1
        
        if(numline[i]==0 and numline[i-1]==0 and numline[i+1]==0):
            res-=1
            continue
            

        numline[i-1]-=1
        numline[i]-=1
        numline[i+1]-=1
        
        rule1= numline[i-1]>=0 or numline[i]>=0 or numline[i+1]>=0
        
        
        print("numline: ", numline, "| res: ", res, "| caseline: ", caseline)

        if(rule1):            
            res+=1
            #caseline[i]=='*'
            continue

        
    
    print("out", res-solid)

#반례 테스트케이스 통과 필요: https://www.acmicpc.net/board/view/45284