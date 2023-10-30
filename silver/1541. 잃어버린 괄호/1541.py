line=input().split("-")
minus_list=[]

for l in line:
    
    if '+' in l:
        plus_list=list(map(int, l.split('+')))
        minus_list.append(sum(plus_list))
    else:
        minus_list.append(int(l))
        
#print(minus_list)

result=minus_list[0]

for num in minus_list[1:]:
    result-=num

print(result)