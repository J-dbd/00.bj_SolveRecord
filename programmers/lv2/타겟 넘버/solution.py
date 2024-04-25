def solution(numbers, target):
    answer = 0

        
    t = len(numbers)-1 #연산 횟수
    ans = []
    
    def recur(curr, cnt, ss):
        if cnt == -1:
            #print(ss)
            ans.append(curr)
            return curr
        else:
            nxt = numbers[cnt]
            recur(curr+nxt, cnt-1, ss+f'+{nxt}')
            recur(curr-nxt, cnt-1, ss+f'-{nxt}')
    
    recur(0, t, "")
    
    #print(ans)
    for an in ans:
        if(an == target):
            answer+=1

    return answer