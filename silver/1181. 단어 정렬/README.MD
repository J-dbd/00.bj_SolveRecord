# 단어 정렬하기 1181

### 포인트

파이썬의 내장 sort를 잘 사용하자

후행 조건을 기준으로 먼저 sort해주어야 한다.

#### 내가 생각해본 코드 (첫 시도)

23.10.18
실패 사유가 뜨진 않았으나 틀렸다.

```python

#{갯수: [단어]} 로 데이터 가공
temp={}
for d in data:
    word=d
    length=len(d)
    if temp.get(length) and (word not in temp[length]):
        temp[length].append(d)
    else:
        temp[length]=[d]

# 갯수별 단어리스트 내부를 정렬
for k,v in temp.items():
    v.sort()

# 갯수 순으로 정렬된, {갯수: [단어들]} 을 원소로 하는 리스트를 리턴
ans_dict=sorted(temp.items())

#정답 출력을 위해 ans_dict을 순회하며 붙임
#이중loop를 피하기 위한 조치
ans=''
for k,v in ans_dict:
    ans+='/'.join(v)
    ans+='/'

#정답 추출을 위해 / 로 나눔
answer=ans.split('/')

#답 추출
for a in answer:
    print(a)


```
