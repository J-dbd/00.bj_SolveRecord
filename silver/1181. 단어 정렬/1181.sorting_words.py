
import sys

#input data
N=int(input())
data=[sys.stdin.readline().strip() for i in range(N)]

#rm duplicates
data=list(set(data))

#sorting by dictionary order (조건 2)
data.sort()

#sorting by length (조건 1)
data.sort(key=len)

#print
print(*data, sep='\n')

#35732	68