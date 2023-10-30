N=int(input())


dparr=[1,2]
def dp_bu(n):
    if n<2: 
        return dparr[n]
    else:
        for i in range(2, N+1):
            temp=(dparr[i-1]+dparr[i-2])%15746
            dparr.append(temp)

    return dparr[n]


print(dp_bu(N-1))

