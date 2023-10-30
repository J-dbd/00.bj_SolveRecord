import sys
data=[]

#엔터 입력 시까지 데이터 삽입 
while True:
    try:
        data.append(int(sys.stdin.readline().strip()))
    except:
        break
    
def post_order(first, end):
    if first>end:
        return
    