import sys
N, K = list(map(int, sys.stdin.readline().strip().split()))

data_dict={}
data_list=[]
for i in range(N): 
    W, V  = list(map(int, sys.stdin.readline().strip().split()))
    vp= round(V/W, 1)
    data_dict[i]=[W, V, vp] # 무게, 가치, 1kg당 가치
    data_list.append([vp, W, V])

#가치 순 정렬
data_list=sorted(data_list, reverse=True)





# def putting(data_list, K):
#     n=len(data_list)
#     dp_v=[0]*n #1차원 array 
#     dp_w=[0]*n
#     for i, data in enumerate(data_list): #1kg당 가치, 무게, 가치
#         print('data', data)
#         print("dp_v", dp_v)
#         print('dp_w', dp_w)
#         vp, v, w = data
        
#         if i ==0 and w<=K:
#             dp_v[i]=v
#             dp_w[i]=w
            
#         else:
#             if dp_w[i-1]<=K-W:
#                 dp_v[i]+=V
#                 dp_w[i]+=W
                
#         print("--------")
    
#     return dp_v, dp_w

# print(putting(data_list, K))
        