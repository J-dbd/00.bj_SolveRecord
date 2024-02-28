import sys
T=int(input())
options=[sys.stdin.readline().strip() for _ in range(T)]

keys = []

def attach_blacket(word):
    return f'[{word}]'

converted_option = ''
res =[]
is_setted = False

for option in options:
    #전체 옵션들
    option_list = option.split()
    #옵션을 어절로 잘라 맨 앞 글자가 있는지 탐색
    for j in range(len(option_list)):
        option_word = option_list[j]
        for i in range(len(option_word)):
            op = option_word[i]
            print(f"op:{op}/i:{i}")
            if(i == 0 and (op[i] not in keys)):
                keys.append(op[0])
                attached_op0 = attach_blacket(op[0])
                if(i>0):converted_option+=" "+attached_op0+op[1:]
                else:converted_option+=attached_op0+op[1:]
                #print("op: ", op, " option_list: ", option_list, " attached_op0: ", attached_op0)
                is_setted = True
            elif(is_setted == False) and (op[i] not in keys):
                keys.append(op[0])
                attached_op0 = attach_blacket(op[0])
                if(i>0):converted_option+=" "+attached_op0+op[1:]
                else:converted_option+=attached_op0+op[1:]

            else:
                if(j>0): converted_option+=" "+op
                else: converted_option+=op
            
    res.append(converted_option)
    converted_option = ''
    print("res", res)
            
            
