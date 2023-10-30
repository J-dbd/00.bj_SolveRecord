'''
메모리 초과!
'''
N=int(input())


dparr=[1,2]
def dp_bu(n):
    if n<2: 
        return dparr[n]
    else:
        for i in range(2, N+1):
            temp=dparr[i-1]+dparr[i-2]
            dparr.append(temp)

    return dparr[n]

answer=dp_bu(N-1)%15746
print(answer)

