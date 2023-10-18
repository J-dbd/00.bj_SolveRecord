import math
T=int(input())
data=list(map(int,input().split()))
#소수 판별 함수
def is_primeNumber(num):
    if num==1:return False #1은 소수가 아니다
    refer_point=int(math.sqrt(num))+1 #기준점이 되는 제곱근
    for i in range(2,refer_point):
        if num%i==0:
            return False
    return True
#소수 개수를 세는 수
cnt_pn=0
#소수 판별하는 반복문
for d in data:
    if is_primeNumber(d):cnt_pn+=1
#답 출력
print(cnt_pn)

#	33240	44