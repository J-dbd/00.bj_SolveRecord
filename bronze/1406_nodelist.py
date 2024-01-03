# 양방향 연결리스트를 구현 
# 

class NodeList:
    def __init__(self, val = 0, data=None, next= None, prev=None):
        self.val=0
        self.data=data
        self.next=next
        self.prev=prev

def add_Node(data, idx, curr_node):
    new_node = NodeList(val=idx, data=data)

    origin_next_node = curr_node.next
    origin_next_node.val +=1
    origin_next_node.prev = new_node
    
    curr_node.next = new_node
    
    return 

def rm_node(idx, target_node):
    prev_node = target_node.prev
    next_node = target_node.next
    
    prev_node.next = next_node
    next_node.prev = prev_node
    next_node.val -=1 #삭제했으니까 
    target_node=None
    
    return 

def search_nodes(head, target_idx):
    node = head
    while(node!=None):
        if(target_idx == node.val):
            return node
        node = node.next

def print_nodes(head):
    node = head
    while(node!=None):
        if(node.val == 0 or node.val ==max_idx): continue
        print(node.data, end='')


commands = {'L':-1, 'D': 1, 'B':0, 'P':''}

origin_strs = list(input())
max_idx = len(origin_strs)
curr_idx = max_idx-1

head = NodeList(0)
tail = NodeList(max_idx)
head.next = tail
tail.prev = head


for i in range(1, max_idx+1):
    #print("i: ", i, "i-1: ", i-1, origin_strs[i-1])
    new_node = NodeList(i)
    new_node.data=origin_strs[i-1]
    new_node.prev = search_nodes(head, i-1)
    search_nodes(head, i-1).next = new_node
    

T = int(input())


for i in range(T):
    cmd_list = input().split()
    cmd = cmd_list[0]
    dx = commands[cmd]
    if (cmd == 'L' or cmd =='D'):
        if(cmd == 'L' and curr_idx<0):continue 
        if(cmd == 'D' and curr_idx == max_idx):continue
        curr_idx += dx

    
    elif(cmd == 'B'):
        if(curr_idx < 0):
            continue
        #origin_strs.pop(curr_idx)
        target_node = search_nodes(head, curr_idx)
        rm_node(curr_idx, target_node)
        
        max_idx-=1
        curr_idx-=1
    
    elif(cmd=='P'):
        #origin_strs.insert(curr_idx+1, cmd_list[1])
        #calc[curr_idx+1] = cmd_list[1]
        print("curr_idx", curr_idx)
        curr_node = search_nodes(head, curr_idx)
        add_Node(cmd_list[1], curr_idx, curr_node)
        max_idx+=1
        curr_idx+=1
    
#print(''.join(origin_strs))
print_nodes(head)

# https://www.acmicpc.net/board/view/54572


# 1) list 의 맨 뒤에서만 삽입/삭제 연산을 할 수 있도록 알고리즘을 구현하기

# 2) 한가운데의 원소를 삽입하거나 삭제했을 때 바로 앞뒤의 원소 이외의 원소를 건드릴 필요가 없는 자료구조를 사용하기
