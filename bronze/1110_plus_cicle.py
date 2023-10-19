import sys
str_num=sys.stdin.readline().strip()

#체크용 저장
origin_num=str_num
cnt=0

while True:
    str_num='0'+str_num #026
    left=str_num[-2]+str_num[-1] #26
    temp=int(left[-2])+int(left[-1]) #(2+6=8)
    right=list(str(temp))[-1] # 8꺼내기 
    str_num=left[-1]+right #합쳐서 다음으로 넘기기
    cnt+=1
    
    if int(str_num)==int(origin_num):
        break

print(cnt)
