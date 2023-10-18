T=int(input())#set step
for t in range(T):
    cnt, str=input().split()
    cnt=int(cnt)
    temp=''
    for s in str:temp+=s*cnt #문자열은 iterable
    print(temp)
    
#2번 중첩 루프
#테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)로 볼 때 
#시간복잡도가 O(n^2)가 되더라도 감당 가능하다고 판단함
