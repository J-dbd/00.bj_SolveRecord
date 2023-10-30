import sys
data=[]

#엔터 입력 시까지 데이터 삽입 
while True:
    try:
        data.append(int(sys.stdin.readline().strip()))
    except:
        break


    
tree={}
class Node:
    def __init__(self, data=None, left_node=None, right_node=None) -> None:
        self.data=data
        self.left_node=left_node
        self.right_node=right_node
# 50 # 30
top_node=Node(data[0])
tree[data[0]]=top_node

size=len(data)

for i in range(1, size):
    print(f"i:{i}/ data[{i}] =  {data[i]} / data[i-1]= {data[i-1]}", end='///')
    if data[i-1]>data[i]:#50 30
        print('1, 왼쪽 노드에 넣음, 2,자기자신노드생성')
        tree[data[i-1]]=Node(data[i-1],data[i])
        tree[data[i]]=Node(data[i])
        print(f" 부모[{data[i-1]}]의 왼쪽노드:",tree[data[i-1]].left_node)
    
        
    if data[i-1]<data[i] and tree[data[i-1]].right_node==None:#5 28
        print('2, 내 바로위노드의 오른쪽에 들어감(없어서)')
        #tree[data[i-1]]=Node(data[i-1], right_node=data[i])
        tree[data[i-3]]=Node(right_node=data[i])
        tree[data[i]]=Node(data[i])
        print(f" 부모[{data[i-1]}]의 오른쪽 노드:",tree[data[i-1]].right_node)
        
    if data[i-1]<data[i] and tree[data[i-1]].right_node!=None:
        print('3, 내 위위노드의 오른쪽에 들어감(바로귀가 있어서)')
        tree[data[i-2]]=Node(data[i-1], right_node=data[i])
        print(f" 위위부모[{data[i-2]}]의 오른쪽 노드:",tree[data[i-2]].right_node)

#print(tree)
    
    
def pre_order(node):
    
    print(node.data)
    
    if node.left_node!=None:
        pre_order(tree[node.left_node])
    if node.right_node!=None:
        pre_order(tree[node.right_node])

#pre_order(tree[data[0]])

# for i in range(size):
#     print(tree[data[i]].data)
#     print(tree[data[i]].left_node)
#     print(tree[data[i]].right_node)
#     print('-------')
    
    

        
