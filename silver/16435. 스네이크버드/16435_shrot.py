N, L = map(int,(input().split()))
fruits = list(map(int, input().split()))
fruits.sort()

for f in fruits:
    if(L>=f):L+=1

print(L)