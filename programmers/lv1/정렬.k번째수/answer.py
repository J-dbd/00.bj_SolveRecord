

def solution(array, commands):
    answer = []
    
    for command in commands:
        start, end, targetIndex = command
        tempArr = array[start-1: end]
        tempArr.sort()
        answer.append(tempArr[targetIndex-1])
    return answer

