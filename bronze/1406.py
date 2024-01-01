# 출력 초과가 뜸 
commands = {'L':-1, 'D': 1, 'B':0, 'P':''}

origin_strs = list(input())
T = int(input())

max_idx = len(origin_strs)
curr_idx = max_idx-1

for i in range(T):
    cmd_list = input().split()
    cmd = cmd_list[0]
    dx = commands[cmd]
    if (cmd == 'L' or cmd =='D'):
        if(cmd == 'L' and curr_idx<0):continue 
        if(cmd == 'D' and curr_idx == max_idx):continue
        curr_idx += dx

    
    elif(cmd == 'B'):
        if(curr_idx < 0):
            continue
        origin_strs.pop(curr_idx)
        print('origin_strs: ', origin_strs)
        max_idx-=1
        curr_idx-=1
    
    elif(cmd=='P'):
        origin_strs.insert(curr_idx+1, cmd_list[1])
        max_idx+=1
        curr_idx+=1
    
print(''.join(origin_strs))




