# 상이 왕에게 도달할 수 있는 최소 이동 횟수
# 도달할 수 없다면 -1 출력

# 상의 위치
si,sj=map(int,input().split())
# 왕의 위치
wi,wj=map(int,input().split())

v=[[0]*9 for _ in range(10)]
from collections import deque

q=deque([(si,sj)])
v[si][sj]=1
choice=[((-1,0),(-1,-1)),((-1,0),(-1,1)),((1,0),(1,-1)),((1,0),(1,1)),((0,-1),(-1,-1)),((0,-1),(1,-1)),((0,1),(1,1)),((0,1),(-1,1))]
while q:
    ci,cj=q.popleft()

    if (ci,cj) == (wi,wj):
        print(v[ci][cj]-1)
        for row in v:
            print(''.join(f'{x:4}' for x in row))
            print(''.join(f'{x:4}' for x in row))
            print(f'{-3f}'row
        break

    flag=False
    for ch in choice:
        di,dj=ch[0][0],ch[0][1]
        ni,nj=ci+di,cj+dj
        if 0<=ni<10 and 0<=nj<9:
            di,dj=ch[1][0], ch[1][1]
            for _ in range(2):
                ni,nj=ni+di,nj+dj
                if ni<0 or ni>=10 or nj<0 or nj>=9:
                    flag=True
                    break
            if flag:
                break
        if 0<=ni<10 and 0<=nj<9 and v[ni][nj] == 0:
            q.append((ni,nj))
            v[ni][nj]=v[ci][cj]+1

else:
    print(-1)
