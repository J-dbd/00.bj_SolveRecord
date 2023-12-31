
# 
N = int(input())

if N==1:
    print("")



# 에라토스테네스의 체 로 소수목록을 구한다 
def find_prime_nums(N):
    all_nums = list(range(2, N+1))
    res = list()
    for num in all_nums: 
        if(num % 2 == 0 and num!=2):
            res.append(num)
            continue
        if(num % 3 == 0 and num!=3):
            res.append(num)
            continue
        if(num % 7 == 0 and num!=7):
            res.append(num)
            continue

    return all_nums
pn_bf_N = find_prime_nums(N)

for i in pn_bf_N:
    while(True):
        if(N % i == 0):
            N = N//i
            print(i)
        
        else: break

# simple solution ############
for n in range(2, N+1):
    if (N % n) == 0:
        while (N % n == 0):
            print(n)
            N = N / n


# time out #################
N = int(input())

if N==1:
    print("")
    

# 에라토스테네스의 체 로 소수목록을 구한다 
def find_prime_nums(N):
    all_nums = list(range(2, N+1))
    res = list()
    for num in all_nums: 
        if(num % 2 == 0 and num!=2):
            res.append(num)
            continue
        if(num % 3 == 0 and num!=3):
            res.append(num)
            continue
        if(num % 7 == 0 and num!=7):
            res.append(num)
            continue

    return all_nums
pn_bf_N = find_prime_nums(N)


for n in pn_bf_N:
    if(N % n == 0):
        N = N//n
        print(n)
        continue
    
