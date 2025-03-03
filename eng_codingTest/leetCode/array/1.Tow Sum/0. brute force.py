def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    #인덱스: 값 인 dict로 만든다.
    #값이 target보다 값이 큰 걸 제한다.=> 음수 경우가 있음
    indexs = []
    for idx in range(len(nums)):
        indexs.append(idx)

    result = []
    
    isgetanswer = False
    
    for index in indexs:
        a = nums[index]
        for idx in indexs:
            if(idx!=index):
                if a + nums[idx] == target:
                    result.append(index)
                    result.append(idx)
                    isgetanswer = True
                    break
            if(isgetanswer):
                break
        if(isgetanswer):
            break
    
    # print('answer ',result)
    # print(result)
    return result

nums = [3,3]
target = 6
twoSum(nums, target)