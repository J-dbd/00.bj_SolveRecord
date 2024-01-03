import sys

numbers = list(map(int, sys.stdin.readline().split()))

num0, num1, num2 = numbers

def calc(num0, num1, num2):
    #num1 이 1이면 num0 ** 1 이 된다.
    if(num1 == 1):
        return num0%num2
    #num1 이 짝수면 num0의 (num1//2)승을 한 뒤 2를 곱해준다. 
    #num1 번 곱하지 않고 그 절반만 곱하고 2를 곱해서 복잡도를 줄인다.
    elif(num1 % 2 ==0):
        return (calc(num0, num1//2, num2)**2)%num2
    #num1 이 홀수면 num1을 나눈 뒤 2를 곱하고 num0을 곱해 num0**num1을 만든다.
    else:
        return ((calc(num0, num1//2, num2)**2)*num0)%num2        
print(calc(num0, num1, num2))