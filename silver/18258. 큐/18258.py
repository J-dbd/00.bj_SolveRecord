class Queue:
    
    def __init__(self) -> None:
        self.queue=[]
        self.front=0
        self.rear=0
        self.size=0
    
    def push(self,val):
        self.queue.append(val)
        self.rear+=1
        self.size+=1
        return
    
    def pop(self):
        if self.size==0:
            return -1
        temp=self.queue[self.front]
        self.front+=1
        self.size-=1
        return temp
    
    def size(self):
        return self.size
    

        