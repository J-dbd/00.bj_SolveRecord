
############ python ############
# import sys
# N=int(input())
# arr=[]

# for i in range(N):
#     arr.append(int(sys.stdin.readline()))

# arr.sort() #직접 배열

# for a in arr:
#     print(a)
##############################

############ quick sort ###################

import sys
N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split()))[0])

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

quick_sort(arr)

print(*arr, sep='\n')


# def quick_sort(arr, left, right):
    
#     pl=left
#     pr=right
#     pivot=int((left+right)//2)
    
#     while pl<=pr:
#         while arr[pl]<arr[pivot]: pl+=1
#         while arr[pr]>arr[pivot]: pr-=1
            
#         if pl<=pr:      
#             arr[pl], arr[pr]=arr[pr], arr[pl]
#             pl+=1
#             pr-=1
    
#     if left<pr: quick_sort(arr, left, pr)
#     if pl<right: quick_sort(arr, pl, right)

         
# quick_sort(arr, 0, len(arr)-1)

# print(*arr, sep='\n')