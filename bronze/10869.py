
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return (a//b)
def res(a,b):
    return a%b

def ans(a,b):
    print(add(a,b))
    print(sub(a,b))
    print(mul(a,b))
    print(div(a,b))
    print(res(a,b))

if __name__=='__main__':
    a,b=map(int,input().split(" "))
    ans(a,b)
    
#함수로 묶어서 보내는 것과 print()로 한 줄 한 줄 처리하는 코드의 차이는 무엇일까?
#이 코드는 31252kb, 40ms의 결과가 나왔다.