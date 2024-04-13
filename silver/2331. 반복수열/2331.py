from collections import deque
D, n = list(map(int, input().split(" ")))
numlist= [D]

mylist =[]

def recur10(num, ten, mylist):
    
    curr_quo = num//ten #몫 495 / 10 = 49
    curr_remains = num % ten #나머지 495 % 10 = 5
    

    if(curr_quo == 0):
        mylist.append(curr_remains)
        return 
    
    else:
        next = curr_quo*ten
        next_ten = 10*ten
        
        mylist.append(num - (curr_quo)*ten)
        
        return recur10(next, next_ten, mylist)

recur10(495, 10, mylist)

print(mylist)