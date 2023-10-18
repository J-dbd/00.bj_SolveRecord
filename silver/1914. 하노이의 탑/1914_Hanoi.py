#하노이의 탑

def hanoi(num, start, end):
    
    '''
    num: 원반 갯수
    start: 출발지
    to:목적지
    other: 다른곳
    '''
    
    if num==0:
        #print(start, end)
        return 
    hanoi(num-1, start, 6-start-end) 
    #가장 큰 원반을 제외한 것들을 원래의 목적지가 아닌 곳으로 이동
    #따라서 other로 들어온 수를
    #to에 넣어주고 to에 들어온 수를 other로 보내어
    #재귀적으로 자기자신을 호출한다(=큰걸 남기고 이동시키고자.)
    #print(f'{start}에서 {to}로 옮긴다')
    print(start, end)
    #가장 큰 원반을 목적지에 이동시키고
    #other자리에 있던 원반뭉치를 
    #똑같은 과정을 통해 to(목적지)로 이동시킨다
    #이 경우 원래 start는 other 자리에 위치하게 된다.
    hanoi(num-1, 6-start-end, end)

N=int(input())
#체크 
cnt=2**N-1
print(cnt)
#함수 실행
if N<=20:hanoi(N,1,3)        
