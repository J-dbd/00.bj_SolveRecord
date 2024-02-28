T = int(input())
options = [input().strip() for _ in range(T)]

keys = []
res = []

for option in options:
    option_lower = option.lower() #소문자로 변환!
    modified_option = option  
    is_setted = False

    #첫 글자 검사
    splited_option = option.split()
    for word in splited_option:
        if (word[0].lower() not in keys):
            keys.append(word[0].lower())
            idx = option_lower.index(word[0].lower()) #옵션 인덱스를 활용해 문자열을 한꺼번에 처리
            modified_option = option[:idx] + "[" + option[idx] + "]" + option[idx+1:] #option의 대소문자를 그대로 써야함
            is_setted = True
            print(modified_option)
            break

    # 첫 글자가 이미 할당되었을 때 
    if not is_setted:
        for i, char in enumerate(option_lower):
            if (char not in keys) and (char.isalpha()):
                keys.append(char)
                modified_option = option[:i] + "[" + option[i] + "]" + option[i+1:]
                print(modified_option)
                break
