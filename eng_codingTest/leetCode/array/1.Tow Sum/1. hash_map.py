def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    hash_map = {}
    
    # value를 hash key로 삼는다. 
    
    for index in range(len(nums)):
        hash_map[nums[index]] = index 
    
    for index in range(len(nums)):
        # nums를 순회하며 제한 값을 추출
        target_comp = target - nums[index]
        
        if(target_comp in hash_map and hash_map[target_comp]!=index):
            # 해시 맵에 기록해둔 값과 일치하는 게 있고 
            # 해시 맵의 값에 넣어둔 기존의 인덱스와 일치여부를 확인(같은 것끼리 하면 안됨)
            return [index, hash_map[target_comp]]
        # 조건을 만족할 때 현재 순회중인 index와 해시의 value를 함께 리턴.
        
        # 만약 만족하는 게 없다면 빈 리스트 리턴.
    return []