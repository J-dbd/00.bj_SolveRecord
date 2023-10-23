js = list(map(int, input().split()))
ss = list(map(int, input().split()))

#역전패란? js가 이기고 있는 순간이 와야 함 
#초 말 개념 알기

def checker(js, ss):
    is_js_win= False
    j_score, s_score = 0,0
    for i in range(9):
        j = js[i]
        j_score+=j
        if(j_score>s_score): is_js_win=True
        s = ss[i]
        s_score+=s
        if(j_score>s_score): is_js_win=True

        
    if(s_score>j_score and is_js_win): 
            return True
    return False

if checker(js, ss): print("Yes")
else: print("No")
