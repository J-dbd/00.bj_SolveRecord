ga, se = list(map(int, input().split()))
T = int(input())
galist = list(range(ga+1))
selist = list(range(se+1))

ga_div, se_div = [], []
for i in range(T):
    f, s = list(map(int, input().split(" ")))
    #tc.append([f,s])
    if(f==0):
        ga_div.append(s)
    else:
        se_div.append(s)

ga_div.sort()
se_div.sort()

se_res, ga_res =[],[]    

for se in se_div:
    se_res.append(galist[:se])
    galist = galist[se:]
    
    #print("selist?", selist)
    if(se==se_div[-1]):
        se_res.append(galist)
        
for ga in ga_div:
    ga_res.append(selist[:ga])
    selist = selist[ga:]
    
    if(ga == ga_div[-1]):
        ga_res.append(selist)


