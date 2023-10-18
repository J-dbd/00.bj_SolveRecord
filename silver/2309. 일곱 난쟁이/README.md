# 일곱 난쟁이 2309

다루는 요소를 줄이는 식으로 생각을 하자!

아래 코드(2309_wrong)은 되지 않았는데 왜 안되었는지 확인이 필요해 보임.

```python
import sys

data=[int(sys.stdin.readline().strip()) for i in range(9)]

data.sort()

# 2개만 구하면 되는 거 아냐?

target=sum(data)-100

print("---")
print(target)

n=len(data)
rm_list=[]
for di in data:
    for dj in data:
        if target==di+dj:
            print("더한 값은?",di, dj)
            rm_list.append(di)
            rm_list.append(dj)
            break



print("rm_list=",rm_list)
data=list(set(data)-set(rm_list))
print(*data,sep='\n')
```
