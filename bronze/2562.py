import sys
#입력받는 데이터
data=[list(map(int,sys.stdin.readline().split()))[0] for i in range(9)]
#최대값, idx 세팅
max_num=data[0]
max_idx=0
for idx, d in enumerate(data):
    if d>max_num:
        max_idx=idx
        max_num=d
    else:continue

print(max_num)
print(max_idx+1)