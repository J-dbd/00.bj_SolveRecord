import sys

data=[int(sys.stdin.readline().strip()) for i in range(9)]

#아홉 난쟁이 들의 키를 모두 더하고 
#넘는 만큼의 키를 가진 2명을 구하면 된다.
#이중loop이므로 o(n^2) 정도는 괜찮을 듯?
#완전탐색으로 GO

#오름차순으로 정렬
data.sort()
#차이 구함
target=sum(data)-100

#반복을 깨뜨려야 하는데
#여기서 외부 스코프에서 이중loop를 걸었더니 
#break가 원하는 때 작동하지 않아 return하는 함수를 제작
#아무거나 출력하는 것이므로 탐색이 끝나 값을 주기만 하면 된다.

temp1, temp2=0,0

for di in data:
    for dj in data:
        if target==di+dj:
            temp1=di
            temp2=dj

data.remove(temp1)
data.remove(temp2)
#출력
print(*data,sep='\n')