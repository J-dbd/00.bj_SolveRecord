s= input()
S = list(s)


# 집합 사용
ss = set()

for i in range(len(S)):
    for j in range(len(S)):
        if(i+j<=len(S)):
            if(i==(i+j)): continue        
            #print(S[i:i+j], '/', i, '-', j)
            ss.add(''.join(S[i:i+j]))
            
#문자열 전체 경우 수 추가
ss.add(s)
print(len(ss))

# dict사용

ans = 0
for i in range(1, len(s)+1):
    temp = dict()
    for j in range(len(s)-i+1):
        if s[j:j+i] not in temp.keys():
            temp[s[j:j+i]] = 1
            ans += 1
print(ans)