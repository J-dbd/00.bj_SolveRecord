#ver1 
score=int(input())
grds=['A','B','C','D','F']

if score>=90 and score<=100: print(grds[0])
elif score>=80 and score<90: print(grds[1])
elif score>=70 and score<80: print(grds[2])
elif score>=60 and score<70: print(grds[3])
else: print(grds[4])

#31120	40
# ! A->F 가 아니라 F->A로 간다면 and가 필요없구나

#ver2
score=int(input())
grds=['A','B','C','D','F']
if score<60:print(grds[4])
elif score<70:print(grds[3])
elif score<80:print(grds[2])
elif score<90:print(grds[1])
else:print(grds[0])
#31120	44 

#ver3
score=int(input())
if score<60:print('F')
elif score<70:print('D')
elif score<80:print('C')
elif score<90:print('B')
else:print('A')
#	31120	40
#  딱히 차이가 없나?