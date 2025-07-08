# 개미가 방향 회전을 N번 하고 멈추는 경우의 수 출력
'''
시작점에서 (-1,0), (1,-1), (1,1) 셋중 선택 가능
(-1,0) 이면 (-1,-1), (-1,1)
(1,-1) 이면 (1,0), (-1,-1)
(1,1) 이면 (-1,1),(1,0)
(-1,-1) 이면 (1,-1), (-1,0)
(-1,1) 이면 (-1,0), (1,1)
(1,0) 이면 (1,-1), (1,1)
'''

N=int(input())
si,sj=0,0
dic={(-1,0):((-1,-1), (-1,1)), (1,-1): ((1,0), (-1,-1)), (1,1):((-1,1),(1,0)), (-1,-1):((1,-1), (-1,0)), (-1,1):((-1,0), (1,1)),(1,0):((1,-1), (1,1))}

from collections import deque
q=deque()

for di,dj in ((-1,0), (1,-1), (1,1)):
    v=set()
    v.add((si,sj))
    v.add((si+di,sj+dj))
    q.append((si,sj,si+di,sj+dj,0,v))

ans=0

while q:
    ci,cj,ei,ej,rotate,st=q.popleft()

    if rotate>=N:
        break

    didj=dic[(ci-ei,cj-ej)]
    flag=False

    for di,dj in didj:
        ni,nj=ei+di,ej+dj

        if (ni,nj) not in st:
            temp=list(st)
            temp.append((ni,nj))
            q.append((ei,ej,ni,nj,rotate+1,set(temp)))
            flag=True

    if not flag and rotate==N:
        ans+=1

print(ans)