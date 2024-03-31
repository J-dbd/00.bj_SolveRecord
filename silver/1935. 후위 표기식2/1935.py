import sys
N = int(input())
expression = list(input())
cmd = dict()


number_stack = []


# 연산자 분리 (cmd로)
for i in range(len(expression)):
    ex = expression[i]
    if(ex.isalpha()):
        cmd[i] = ex

alpha2num = dict()
for k,v in cmd.items():
    alpha2num[v] = int(input())


#사칙연산 계산 함수
def calculate(s, f, e):
    if s=='*': return f*e
    elif s=='/': return (f/e)
    elif s == '+': return f+e
    elif s=='-': return f-e


print('alpha2num', alpha2num) #res {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

converted_expression = [] 
for ex in expression:
    if ex in alpha2num.keys():
        converted_expression.append(alpha2num[ex])
        continue
    else:
        converted_expression.append(ex)
 
print('ans', converted_expression) #ans [1, 2, 3, '*', '+', 4, 5, '/', '-']




print(expression)