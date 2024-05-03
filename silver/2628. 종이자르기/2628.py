garo, sero = list(map(int, input().split(" ")))
T = int(input())

garo_div, sero_div = [],[]
for _ in range(T):
    a, b = list(map(int, input().split()))
    
    if(a==1):garo_div.append(b)
    elif(a==0):sero_div.append(b)

garo_div.sort()
sero_div.sort()

garo_list = list(range(garo+1))
sero_list = list(range(sero+1))

#print("가로로 sero 리스트를 자를 것:", sero_div, "세로로 garo 리스트를 자를 것", garo_div)
#print(sero_list, garo_list)

garo_divied, sero_divied = [],[]


def spliter(lst, indices):
    result = []
    start = 0
    
    for idx in indices:
        result.append(lst[start:idx+1])
        start = idx
    
    result.append(lst[start:])
    
    answer = []
    for res in result:
        answer.append(len(res)-1)
    return answer



seros= spliter(sero_list, sero_div)
garos= spliter(garo_list, garo_div)
ans = []
for ser in seros:
    for gar in garos:
       ans.append(ser*gar)

print(max(ans)) 
