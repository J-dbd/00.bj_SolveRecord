def findHansu(number):
    numlist =list(map(int, list(number)))
    #print(numlist)
    
    if(len(numlist)<=2):
        return False
    
    dp = [0]*(len(numlist))
    if(len(numlist)>=2):
        dp[0] = numlist[1]-numlist[0]
    else:
        return False 
    
    for i in range(2, len(numlist)):
       # print(i, "/", numlist[i], numlist[i-1])
        temp = numlist[i]-numlist[i-1]
        dp[i] = temp
        
        if(dp[i]!=dp[i-1]):
            return False
        
    return True

    
    
    
target = int(input())
cnt = 0
for i in range(1, target+1):
    if(findHansu(str(i))):
        cnt+=1
    
print(cnt)


'''
123


'''