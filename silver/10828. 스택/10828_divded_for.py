import sys

N=int(input())
commands=[sys.stdin.readline().split() for _ in range(N)]

my_stack=[]

def my_push(n): #push
    return my_stack.append(n)

def get_pop(): #pop
    if len(my_stack)!=0:
        return my_stack.pop()
    return -1

def get_size(): #size
    return len(my_stack)

def is_empty(): #empty
    if len(my_stack)==0:
        return 1    
    return 0
def get_top(): #top
    if len(my_stack)!=0:
        return my_stack[-1]
    return -1


for command in commands:
    if command[0]=='pop':
        print(get_pop())
    elif command[0]=='size':
        print(get_size())
    elif command[0]=='empty':
        print(is_empty())
    elif command[0] == 'top':
        print(get_top())
    elif command[0] =='push':
        my_push(int(command[1]))

