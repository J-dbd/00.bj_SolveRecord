import sys

N=int(input())
stack=[]
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0]=='push':
        stack.append(int(command[1]))
    elif command[0]=='pop':
        print(-1) if len(stack)==0 else print(stack.pop())
    elif command[0]=='size':
        print(len(stack))
    elif command[0]=='empty':
        print(1) if len(stack)==0 else print(0)
    elif command[0]=='top':
        print(stack[0]) if len(stack)!=0 else print(-1)
    