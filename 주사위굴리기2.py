''' 2차풀이
[0] 타임라인
구상 (20분)
구현 (10분)
디버깅 (5분)

[1] 실수한 점
1. 범위 밖을 나가면 방향 바꿔주라는 문제 조건 누락

[2] 배울점

'''
# NxN 격자, M번 굴리기
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
score=0
# 상,우,하,좌
dic={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
ball=[5,4,1,3,6,2]
d=1
si,sj=0,0

# ======
from collections import deque

for _ in range(M):
    di,dj=dic[d]
    ni,nj=si+di,sj+dj

    if 0<=ni<N and 0<=nj<N:
        si,sj=ni,nj
    else:
        d=(d+2)%4
        di,dj=dic[d]
        si,sj=si+di,sj+dj

    if d == 0:
        ball=[ball[2],ball[1],ball[5],ball[3],ball[0],ball[4]]

    elif d == 1:
        ball = [ball[0], ball[4], ball[1], ball[2], ball[3], ball[5]]

    elif d == 2:
        ball = [ball[4], ball[1], ball[0], ball[3], ball[5], ball[2]]

    else:
        ball = [ball[0], ball[2], ball[3], ball[4], ball[1], ball[5]]

    q=deque([(si,sj)])
    v=[[0]*N for _ in range(N)]
    v[si][sj]=1
    cnt=1

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==arr[ci][cj] and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1

    score+=arr[si][sj]*cnt

    if ball[4] > arr[si][sj]:
        d=(d+1)%4
    elif ball[4] < arr[si][sj]:
        d=(d-1)%4

print(score)

'''
주사위굴리기2 (1/64) / 2025-03-05 / 체감 난이도 : 골드 4
소요 시간 : 1시간 / 시도 : 1회 / 실행 시간 : 172ms / 메모리 : 114372KB

[타임라인]
1. 문제 이해 & 구상 & sudo code 작성 (45분)
2. 구현 (15분)

[디버깅 내역]
- 인접한 숫자가 총 몇개 있는지 구하는 로직에서, 총 개수를 세는 것이 아니라 깊이로 관리했다
그래서 count가 잘못됐다

[구상]
옛날에 혜민프로님이 규칙 찾아서 간단하게 썼던 기억이 어렴풋이 나서 .. (뭐였는지는 기억 안 나고 ㅜ 정리하고 넘어가아 제발)
전개도에서 규칙을 찾아서 회전시킬까 했는데.. 바로 안 보여서 일단 그냥 좌표로 했다...
다른 코드 보고 배워야 한다 !!!

[후기]
아이디어를 다양하게 내 볼 필요가 있다 (다른 코드의 도움을 받으며)
자꾸 같은 방식 (주로 비효율적인)을 하니까 안 는다

'''
from collections import deque

def bfs(si,sj,pivot):
    q=deque()
    q.append((si,sj))
    v=[[0]*M for _ in range (N)]
    v[si][sj]=1
    cnt=1
    while q:
        ci, cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==pivot and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1
    return cnt

# 행, 열, 이동횟수
N,M,K=map(int,input().split())

# 점수가 써져있는 판
arr=[list(map(int,input().split())) for _ in range(N)]

di=[0,1,0,-1]
dj=[1,0,-1,0]

# 초기 위치와 방향
si,sj,dr=0,0,0

# 초기 주사위
ball=[[0,2,0],[4,1,3],[0,5,0],[0,6,0]]

k=0

# 총 결과물
ans=0

while k<K:
    # 이동횟수 한 번 늘리고
    k+=1
    # [1] 이동 방향으로 한칸 굴러간다
    ni, nj = si + di[dr], sj + dj[dr]
    # 즉, 범위 밖이면
    if ni < 0 or ni >= N or nj < 0 or nj >= M:
        # 더해줬으니까 원상복구하고
        ni, nj = si - di[dr], sj - dj[dr]
        # 방향 바꾸고
        dr=(dr+2)%4
        # 다시 이동
        ni, nj = si + di[dr], sj + dj[dr]

    # 결국 최종 dr을 따르면 됨
    new_ball = [[0] * 3 for _ in range(4)]
    if dr == 0:  # 동
        new_ball[0][1] = ball[0][1]
        new_ball[1][0] = ball[3][1]
        new_ball[1][1] = ball[1][0]
        new_ball[1][2] = ball[1][1]
        new_ball[2][1] = ball[2][1]
        new_ball[3][1] = ball[1][2]

    elif dr == 1:  # 남
        new_ball[0][1] = ball[3][1]
        new_ball[1][0] = ball[1][0]
        new_ball[1][1] = ball[0][1]
        new_ball[1][2] = ball[1][2]
        new_ball[2][1] = ball[1][1]
        new_ball[3][1] = ball[2][1]

    elif dr == 2:  # 서
        new_ball[0][1] = ball[0][1]
        new_ball[1][0] = ball[1][1]
        new_ball[1][1] = ball[1][2]
        new_ball[1][2] = ball[3][1]
        new_ball[2][1] = ball[2][1]
        new_ball[3][1] = ball[1][0]

    else:  # 북
        new_ball[0][1] = ball[1][1]
        new_ball[1][0] = ball[1][0]
        new_ball[1][1] = ball[2][1]
        new_ball[1][2] = ball[1][2]
        new_ball[2][1] = ball[3][1]
        new_ball[3][1] = ball[0][1]

    # 현재 위치 바꿔주고
    si, sj = ni, nj

    # 주사위도 바꿔주고
    ball=new_ball

    # [2] 점수를 획득한다
    result = bfs(si, sj, arr[si][sj])
    ans += arr[si][sj] * result

    # [3] 주사위의 아랫면과 비교해서 방향을 확인한다
    bottom=ball[3][1]
    if bottom > arr[si][sj]:
        dr = (dr + 1) % 4
    elif bottom < arr[si][sj]:
        dr = (dr - 1) % 4
print(ans)