# 1978 primeNum_sqrt 
import sys
import math

########################################### 
# TYPE1                                   #
# 소수 판별과 partition함수를 사용하는 방법  #
###########################################

    
########################  
# sys.stdin.readline() #
# 33240	160            #
########################

T=int(input()) #test case num

#data를 받아둠 (O(n))
data=[list(map(int,sys.stdin.readline().split()))[0] for i in range(T)]

#소수 판별
def is_primeNum(num):
    refer_num=int(math.sqrt(num))+1
    if num==1: return False
    for i in range(2,refer_num):
        if num%i==0:return False
    return True

#partition을 찾는 함수 (O(n))
def find_partition(d):
    median=d//2
    pn=median
    mn=median
    for i in range(d):
        if is_primeNum(pn) and is_primeNum(mn):  
            print(mn,pn)
            return 
        else:
            pn+=1
            mn-=1
            

for d in data:
    find_partition(d)

    
##############  
# input으로  #
# 33240	608  #
#############

T=int(input()) #test case num
#소수 판별 함수
def is_primeNum(num):
    refer_num=int(math.sqrt(num))+1
    if num==1: return False
    for i in range(2,refer_num):
        if num%i==0:return False
    return True
#한줄 한줄 input으로 받기
for i in range(T):
    num=int(input())
    median=num//2
    pn=median
    mn=median
    for i in range(num):
        if is_primeNum(pn) and is_primeNum(mn):  
            print(mn,pn)
            break
        else:
            pn+=1
            mn-=1
            
            
########################################### 
# TYPE2                                   #
# 미리 모든 소수 리스트를 뽑아놓는 방법      #
###########################################

#4 ≤ n ≤ 10,000
#	31120	80

#에라토스테네스의 체 생성
prime_num_list=[False,False]+[True]*10000
# index가 0과 1은 소수가 아니다. 
# 2~10001까진 소수로 가정

for i in range(2,101):#제곱근까지의 범위만 체크.
    if prime_num_list[i]:
        j=2
        while i*j<=10001:
            prime_num_list[i*j]=False
            j+=1
            
            
T=int(input())
data=[list(map(int,sys.stdin.readline().split()))[0] for i in range(T)]

for d in data:
    median=d//2
    plus_num=median
    minus_num=median
    for i in range(d): #d(값)번 반복해야 함
        if prime_num_list[minus_num] and prime_num_list[plus_num]:
            print(minus_num, plus_num)
            break
        else:
            plus_num+=1
            minus_num-=1