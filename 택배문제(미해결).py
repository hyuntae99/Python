N, C = input().split()
N, C = int(N), int(C) # 마을 수, 트럭 용량
M = int(input()) # 박스 정보 개수
lists = []
for i in range(M):
    lists.append([])
    send, take, many = input().split()
    lists[i].append(int(send))
    lists[i].append(int(take))
    lists[i].append(int(many))
lists.sort(key=lambda x: (x[1], x[0])) 

global cnt, tr
cnt = 0
tr = 0

for i in range(1, N+1):
    for j in range(M):
        
        if int(lists[j][1]) == i:
            for k in range(1, int(lists[j][2])+1):
                if tr > 0:
                    tr -= 1  
                    cnt += 1  
                    
        if int(lists[j][0]) == i:
            for k in range(1, int(lists[j][2])+1):
                if tr < C:
                    tr += 1
 
print(cnt)