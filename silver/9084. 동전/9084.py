import sys 

T= int(input())
data=[]
temp_dict={}
for i in range(T):
    N=int(input()) # 동전의 가짓수 
    temp=list(map(int, sys.stdin.readline().strip().split()))
    
    
    
    target=int(input())
    temp_dict[target]=temp
    data.append(temp_dict)
    temp_dict={}
    
    

print(data)

#배낭 문제로 풀어보자!
