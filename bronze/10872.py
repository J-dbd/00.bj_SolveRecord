#팩토리얼 
N=int(input())
def factorial(n):
    if n<=1:
        return 1
    
    return n*factorial(n-1)

print(factorial(N))

#31120	40