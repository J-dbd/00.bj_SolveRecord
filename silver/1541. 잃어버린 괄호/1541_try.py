'''
시도한 접근방향 : 숫자마다 + / -를 각자 붙여보기 
그런데 이게 아닌듯하다. 왜냐하면 괄호를 치는 것이기 때문에..
'''


sign=['+','-']
line=input()

num_list=[]
sign_list=[]
temp=''

for i in range(len(line)):
    if line[i] not in sign:
        temp+=line[i]
        
    else:
        num_list.append(int(temp))
        sign_list.append(line[i])
        temp=''
        
    if i==len(line)-1 and temp!='':
        num_list.append(int(temp))
        

print(num_list)
print(sign_list)

for i in range(len(sign_list)):
    if sign_list[i]=='-':
        num_list[i+1]=num_list[i+1]*(-1)

print(num_list)
        
        
        
        
    
    