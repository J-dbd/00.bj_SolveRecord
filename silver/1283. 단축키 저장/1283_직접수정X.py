T = int(input())

setted_keys = []
for _ in range(T):
    options = list(input().split()) #['Save', 'All']
    is_setted = False
    
    for option in options:
        if(option[0].lower() not in setted_keys):
            setted_keys.append(option[0].lower())
            is_setted = True
            option = '['+option[0]+']'+option[1:]
            print("option? ", option)
            print(' '.join(options))
            break
            
    if(not is_setted):
        #옵션 단어의 첫글자가 단축키가 아님
        #옵션 단어 전체 알파벳 순회 시작
        #flag설정
        
        
        for i in range(len(options)):
            checked = False
            for j in range(len(option)):
                if(option[i].lower() not in setted_keys):
                    setted_keys.append(option[i].lower())
                    checked = True
                    is_setted = True
                    option = option[0:i] + '[' + option[i] + ']' + option[i+1:]
                    print("option?", option)
                    print(' '.join(options))
                    break
            if checked: break
            
    if(not is_setted): print(' '.join(options))

            
            
    
    
    