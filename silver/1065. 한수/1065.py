def findHansu(number):
    numlist =list(map(int, list(number)))
    #print(numlist)
    
    
    diff = numlist[1]-numlist[0]

    
    for i in range(2, len(numlist)):
       # print(i, "/", numlist[i], numlist[i-1])
        if(numlist[i]-numlist[i-1]!=diff):
            return False
        
    return True

    
    
    
target = int(input())
cnt = 0
for i in range(1, target+1):
    if(i<=99):
        cnt+=1
    elif(findHansu(str(i))):
        cnt+=1
    
print(cnt)


'''
123


'''