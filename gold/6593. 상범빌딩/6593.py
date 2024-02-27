#최단거리이므로 BFS

from collections import deque
import sys
input = sys.stdin.readline

# 3차원 배열 Input
while True:
    L, R, C = map(int, input().split())
    #층수, 한 층의 행, 한 층의 열
    if L==0 or R==0 or C==0: break
    
    building = []
    visited = [[[False] * C for _ in range(R)] for _ in range(L)] #for BFS
    
    
    for _ in range(L):
        floor = [list(input().strip()) for _ in range(R)] 
        building.append(floor)
        input() # 각 층 사이 빈 줄 읽어서 넘기기
    
    #print("building", building)
        



