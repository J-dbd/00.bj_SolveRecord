import sys
n=int(input())
N=sys.stdin.readline().split()
m=int(input())
M=sys.stdin.readline().split()

#이진탐색

#이진탐색을 위한 정렬
N.sort()

#이진탐색 시작
def binary_search(arr, target):
    n=len(arr)
    pl=0
    pr=n-1
    
    while True:
        pivot=int((pl+pr)//2)
        if target==arr[pivot]:
            #return pivot #검색 성공
            return 1
        elif target>arr[pivot]:
            pl=pivot+1 #크다면 pl을 pivot뒤로
        else:
            pr=pivot-1 #작다면 pr을 pivot앞으로
        
        if pl>pr: #pl이 pr보다 크다면 검색이 끝나야 함
            break
    
    return 0

for m in M:
    print(binary_search(N,m))

            
        
    