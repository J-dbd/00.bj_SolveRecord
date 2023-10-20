import sys
n, k=list(map(int, sys.stdin.readline().split()))

circle=list(range(1,n))

result=[]
def circulate(circle, k):
    if len(circle)<=k:
        result.extend(circle)
        return
    result.append(circle.pop(k-1))
    circle=circle[k:]+circle[:k-1]
    return circulate(circle,k)
    
circulate(circle,k)
print(result)