import sys
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))

#연속합은 nums 자체가 dp가 된다. 
#이전값과의 값 중 최대값인 것들만 기록해두게 되므로 
#1부터 시작하는 건 index가 0인 것은 그 혼자 선택되었을때이기 때문이다. 

def find_cnti_sum(N, nums):
    if(N==1):
        return nums
    else: #nums의 개수가 1보다 클 때
        for i in range(1, N):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
            
        return nums
    
ans = find_cnti_sum(N, nums)

print(max(ans))