'''
매초 한칸, 전과 같은 방향이면 가속도 -> 전보다 1칸 더 갈 수 있다
1초 후 지도 밖이면 갈 수 없는 거

도착하는 시간이 달라지니까 visited에 시간을 기록해야하고
같은 좌표에 같은 방향으로 시간이 더 빨리 온게 살아 남는다
#  방향, 몇번 가는지? 좌표

visited를 어떻게 관리할까
더 많은 칸으로 갔다고 무조건 좋은 건 아니니까
몇 mul로 왔는지가 중요

'''

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

from collections import deque
# 상 우 하 좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

q=deque([(-1,0,0,0,[(0,0)])])
v=[[[float('inf')]*4 for _ in range(N)] for _ in range(N)]
v[0][0]=[0,0,0,0]
mn=float('inf')

while q:
    dr,mul,ci,cj,lst=q.popleft()

    if (ci,cj) == (N-1,N-1):
        mn=min(mn,v[ci][cj][dr])

    # 위 변수들의 의미는
    # ci,cj의 좌표에 time시간이 걸려서 왔고, dr의 방향을 사용했고,mul 반복을 사용했다
    # 만약 dr == d 일때, mul+1을 가는 거고
    # 아니라면 다 1씩만 가는 거
    # mul+1 갈 때는 그래도 구역 갈 수 있는지 확인해야하고
    # 이건 현재 시간이랑 time+1 이랑 비교를 해야하
    for d in (0,1,2,3):
        si, sj = ci, cj
        di,dj=dx[d],dy[d]

        # 만약 방향이 같다면
        if dr==d:
            ml=mul+1
        else:
            ml=1

        for m in range(ml):
            ni,nj=si+di,sj+dj
            # 같아도 못 들어감
            # 그럼 거쳐 가는 애들 vs 거기가 도착인 애들? 도착인 애들만 비교하면 됨
            # 1초에 여러칸이면 그래도 1초 지난 거랑 비교해야겠나?
            # 갈 때는 크거나 같으면 되고, 도착한 곳은 크기만 해야함
            if 0<=ni<N and 0<=nj<N:
                if m == ml-1: # 여기가 이상해
                    if (arr[ni][nj]!=0 and arr[ni][nj]<=v[ci][cj][dr]+1):
                        break
                else:
                    if (arr[ni][nj] == 0 or arr[ni][nj]>=v[ci][cj][dr]+1):
                        si, sj = ni, nj
                    else:
                        break
            else:
                break
        else:
            if v[ni][nj][d]>v[ci][cj][dr]+1:
                # ni,nj에 최종 목적지가
                q.append((d,ml,ni,nj,lst+[(ni,nj)]))
                v[ni][nj][d]=v[ci][cj][dr]+1

if mn == float('inf'):
    print("Fired")
else:
    print(mn)


