
# 양방향 연결리스트를 구현 
import sys

# 1. node 선언
class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=self
        self.prev=self
    def __str__(self):
        return str(self.data)

# 2. doublely linked list 선언

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        
    def __iter__(self):
        node = self.head.next
        while(node != self.head):
            yield node
            node = node.next
    
    def __str__(self):
        return "".join(str(node.data) for node in self)

    def splice(self, x, y, given):

        if x==None or y==None or given==None: return
        # 1. x, y 를 특정지어 전달하면 해당 구간을 자른다. 
        x.prev.next = y.next
        y.next.prev = x.prev
        
        # 2. 잘라낸[x, y]를 given 다음에 삽입하기?
        given.next.prev = y
        y.next = given.next
        x.prev = given 
        given.next = x 
        
    def moveAfter(self, x, given):
        self.splice(x, x, given)
    
    def moveBefore(self, x, given):
        self.splice(x, x, given.prev) 
    
    def insertBefore(self, a, data):
        self.moveBefore(Node(data), a)
    
    def deleteNode(self, x):
        if x == None or x == self.head: return #삭제 불가 
        # ... xp x xn 
        x.prev.next = x.next 
        x.next.prev = x.prev


L = DoublyLinkedList()
cursor = Node('|')

cursor.next = L.head
cursor.prev = L.head
L.head.next = cursor
L.head.prev = cursor

text = list(sys.stdin.readline().strip())

#set data
for t in text:
    #print("t in text", t)
    L.insertBefore(cursor, t)
    
T = int(sys.stdin.readline().strip())

for i in range(T):
    cmd_list = sys.stdin.readline().strip().split()
    cmd = cmd_list[0]

    if(cmd == 'L' and cursor.prev.data!=None):
        L.moveBefore(cursor, cursor.prev)
    
    elif(cmd == 'D' and cursor.next.data!=None):
        L.moveAfter(cursor, cursor.next)
    
    elif(cmd == 'B' and cursor.prev.data!= None):
        L.deleteNode(cursor.prev)
    
    elif(cmd == 'P'):
        L.insertBefore(cursor, cmd_list[1])
        
#delete cursor
L.deleteNode(cursor)

print(L)
