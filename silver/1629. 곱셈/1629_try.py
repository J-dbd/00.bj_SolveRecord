import sys

numbers = list(map(int, sys.stdin.readline().split()))

num = numbers[0]
for i in range(numbers[1]):
    num = (num*num)%numbers[2]

print(num)