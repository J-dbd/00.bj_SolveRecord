T = int(input())

setted_keys = []
for _ in range(T):
    options = input().split() 
    is_setted = False
    
    for i, option in enumerate(options):
        if option[0].upper() not in setted_keys:
            setted_keys.append(option[0].upper())
            is_setted = True
            options[i] = '[' + option[0] + ']' + option[1:] 
            print(' '.join(options))
            break
            
    if not is_setted:
        for i, option in enumerate(options):
            for j in range(len(option)):
                if option[j].upper() not in setted_keys:
                    setted_keys.append(option[j].upper())
                    is_setted = True
                    options[i] = option[:j] + '[' + option[j] + ']' + option[j+1:] 
                    print(' '.join(options))
                    break
            if is_setted:
                break
                
    if not is_setted:
        print(' '.join(options))