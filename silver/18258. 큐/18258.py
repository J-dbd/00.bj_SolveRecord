import sys
class Queue:
    
    def __init__(self) -> None:
        self.queue=[]
        self.front=0
        self.rear=0
        self.size=0
    
    def enqueue(self,val): #enqueue
        self.queue.append(val)
        self.rear+=1
        self.size+=1
        return
    
    def dequeue(self):
        if self.size==0: return -1
        temp=self.queue[self.front]
        self.front+=1
        self.size-=1
        return temp
    
    def size_(self):
        return self.size
    
    def empty(self):
        if self.size==0:return 1
        else: return 0
        
    def front_(self):
        if self.size==0: return -1
        return self.queue[self.front]
    
    def back_(self):
        if self.size==0: return -1
        return self.queue[self.rear-1]
    

N=int(input())
queue=Queue()
for i in range(N):
    command=sys.stdin.readline().strip().split()
    if command[0]=='push':
        queue.enqueue(int(command[1]))
    elif command[0]=='pop':
        print(queue.dequeue())
    elif command[0]=='size':
        print(queue.size_())
    elif command[0]=='empty':
        print(queue.empty())
    elif command[0]=='front':
        print(queue.front_())
    elif command[0]=='back':
        print(queue.back_())

