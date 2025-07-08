'''
헷갈리는 부분:
- " 위의 네 단계에서 최단 경로를 계산할 때는 맨해튼 거리를 기준으로 합니다 "
-> 매두사가 갈 때는 맨해튼 거리를 기준으로 최단 경로를 결정할 수 없지 않은데 이게 뭔소리임
- 8방향 나눈다는건도 몬소린지 모르겠음

-덱은 플러스 연산이 안됨 !!!!
'''


def my_print():
    for row in arr:
        print(*row)
    print('---')
    for row in p:
        print(*row)
    print('---')
    print(p_loc)
    print('---')


# ===========================================================
# 마을의 크기, 전사의 수
N, M = map(int, input().split())

# 메두사의 초기 위치, 최종 도달해야하는 위치
si, sj, ei, ej = map(int, input().split())

# ==========================================================

# 전사와 관련해서는 두개로 관리
p = [[[] for _ in range(N)] for _ in range(N)]  # 여러명이 들어갈 수도 있고
p_loc = [[False, False, -1, -1]]  # 아예 사라졌는지?, 돌이 됐는지?
idx = 1
_ = list(map(int, input().split()))

for i in range(0, 2 * M - 1, 2):
    p_loc.append([False, False, _[i], _[i + 1]])
    p[_[i]][_[i + 1]].append(idx)
    idx += 1

arr = [list(map(int, input().split())) for _ in range(N)]

# ====================================================
from collections import deque


# 메두사의 최단 경로를 구하는 함수
def bfs(si, sj, ei, ej):
    q = deque([(si, sj, [])])  # 목적지까지 갈 때 어떤 방향을 선택해야하는지 넣어둔다
    # 나중에 appendleft로 하나하나 빼면서 갈거임
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1

    while q:
        ci, cj, route = q.popleft()

        if (ci, cj) == (ei, ej):
            return deque(route)

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상,하,좌,우 우선순위를 둔다
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and v[ni][nj] == 0:  # 범위내, 도로만, 방문 놉
                q.append((ni, nj, route + [(di, dj)]))
                v[ni][nj] = 1
    return -1


# ============================================================

# 맨해튼 거리를 구하는 함수
def dist(si, sj, ei, ej):
    return abs(si - ei) + abs(sj - ej)


# ============================================================

# 만약 처음부터 갈 수 없다면 -1을 출력하고 끝낸다
if bfs(si, sj, ei, ej) == -1:
    print(-1)
else:
    route = bfs(si, sj, ei, ej)

    while True:
        # [1] 메두사의 이동
        di, dj = route.popleft()  # 이번에 갈 방향은?
        if not route:  # 마지막이면 끝낸다 !
            print(0)
            break
        si, sj = si + di, sj + dj  # 새로 바뀐 메두사의 위치

        if p[si][sj] != []:  # 전사 누군가가 있다면?
            for idx in p[si][sj]:
                p_loc[idx][0] = True  # 다 죽은 거 처리하고
            p[si][sj] = []  # 죽었으니까 맵도 비운다

        my_print()
        # ========================================================================
        # [2] 메두사의 시선
        # 상, 하, 좌, 우 순서
        dic = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}


        def sight(si, sj, d):
            mi, mj = si, sj  # 메두사의 위치
            see = [[0] * N for _ in range(N)]  # 시선이 닿는 곳
            di, dj = dic[d]  # 방향
            si, sj = si + di, sj + dj  # 보는 방향으로 한 칸 내려가고
            stone = []  # 돌이 되어야 하는 전사 좌표 -> 돌 해제시키기 편하려고 리스트에 담아둠
            see[mi][mj] = 9  # 메두사 있는 곳
            ans = 0

            if d in (0, 1):  # 상, 하의 경우에 양 옆으로 퍼질 거고
                spread = [(0, 1), (0, -1)]
            else:  # 좌, 우의 경우에 위 아래로 퍼질 거야
                spread = [(1, 0), (-1, 0)]

            for mul in range(1, 30):  # 50 x 50 이라고 하더라도 25에서 끊키니까 넉넉잡아 30까지로 함
                if 0 <= si < N and 0 <= sj < N:  # 범위 내일 때까지
                    see[si][sj] = 1  # 지금 있는 곳 1로 표시하고
                    for m in range(1, mul + 1):  # mul번 옆으로 퍼진다
                        for ddi, ddj in spread:
                            if 0 <= si + ddi * m < N and 0 <= sj + ddj * m < N:  # 범위 내일때만
                                see[si + ddi * m][sj + ddj * m] = 1  # 1로 표시
                    si, sj = si + di, sj + dj  # 하나씩 내리고 더 커진 mul을 가지고 또 퍼짐
                else:
                    break
            # ===============================================================================================
            # 잠시 돌릴게 나중에 반대로 다시 돌림
            if d == 0:  # 상이면 x축으로 뒤집어
                see = [row[::-1] for row in see[::-1]]

            elif d == 2:  # 좌이면 반시계 90도 회전
                see = list(map(list, zip(*see)))[::-1]

            elif d == 3:  # 우이면 90도 회전
                see = list(map(list, zip(*see[::-1])))

            # 메두사 위치 mi,mj
            for a, b in ((1,-1),(1,0),(1,1)):
                mmi,mmj=mi+a,mj+b
                flag = False
                while 0 <= mmi < N and 0 <= mmj < N:
                    if flag:
                        see[mmi][mmj] = 0  # 0은 시야 안 닿는 곳임
                    if len(p[mmi][mmj]) == 1:  # 전사가 있다면?
                        stone.append((mmi, mmj))
                        ans += len(p[mmi][mmj])
                        for idx in p[mmi][mmj]:
                            p_loc[idx][1] = True
                        flag = True
                    mmi,mmj=mmi+a,mmj+b

            for i in range(mi + 1, N):
                for j in range(mj):
                    if see[i][j] == 1 and len(p[i][j]) == 1:
                        stone.append((i, j))
                        ans += len(p[i][j])
                        for idx in p[i][j]:
                            p_loc[idx][1] = True
                        # i,j부터 왼쪽 대각선과 그 좌표 일직선 사이는 다 0으로 바꾸기
                        for x in range(i+1,N):
                            for y in range(0,j+1):
                                if see[i][j]==1 and j <= y <= -x + (i + j):
                                    see[i][j]=0

            for i in range(mi + 1, N):
                for j in range(mj + 1, N):
                    if see[i][j] == 1 and len(p[i][j]) == 1:
                        stone.append((i, j))
                        ans += len(p[i][j])
                        for idx in p[i][j]:
                            p_loc[idx][1] = True
                        # 좌표 일직선부터 오른쪽 대각선 사이는 다 0으로 바꾸기
                        for x in range(i+1,N):
                            for y in range(j,N):
                                if see[i][j]==1 and j <= y <= x:
                                    see[i][j]=0
            if d == 0:  # 상이면 x축으로 뒤집어
                see = [row[::-1] for row in see[::-1]]

            elif d == 2:  # 좌이면 반시계 90도 회전
                see = list(map(list, zip(*see[::-1])))

            elif d == 3:  # 우이면 90도 회전
                see = list(map(list, zip(*see)))[::-1]

            return ans, stone, see
            # 이 함수에서 return 하는 거는 돌로 만드는 전사들



        mx = 0
        change_stone=[]
        ssight=[[0]*N for _ in range(N)]
        for d in range(0, 4):
            ans, stone, see = sight(si, sj, d)
            if ans > mx:
                mx = ans
                change_stone = stone[:]
                ssight = [row[:] for row in see]

        print('시선 끝나고 나서')
        my_print()

        move_dist=0
        attack_m=0

        for idx in range(1,len(p_loc)):
            if not p_loc[idx][0] and not p_loc[idx][1]:
                _,_,r,c=p_loc[idx]
                ni,nj=r,c
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ri,rj=r+di,c+dj
                    if 0<=ri<N and 0<=rj<N and dist(ri,rj,si,sj)<dist(r,c,si,sj) and ssight[ri][rj]==0:
                        ni,nj=ri,rj

                # 끝나면 ri,rj가 정해져있겠지?
                if (ni,nj) != (r,c):        # 움직일 수있다는 거니까
                    move_dist+=1
                    if (ni,nj) == (si,sj):
                        attack_m+=1
                        p_loc[idx][0]=True
                        continue
                    else:                   # 아니라면 한 칸 더 간다
                        nii,nnj=ni,nj
                        for di, dj in ((0, -1), (0, 1),(-1, 0), (1, 0)):
                            rii, rjj = ni + di, nj + dj
                            if 0 <= rii < N and 0 <= rjj < N and dist(rii, rjj, si, sj) < dist(ni, nj, si, sj) and ssight[rii][rjj] == 0:
                                nni,nnj=rii,rjj
                        # 끝나면 ri,rj가 정해져있겠지
                        if (nii,nnj) != (ni,nj):
                            move_dist += 1
                            if (nii, nnj) == (si, sj):
                                attack_m += 1
                                p_loc[idx][0] = True
                                continue

                                p[r][c].remove(idx)
                                p_loc[idx][2], p_loc[idx][3] = nii,nnj
                                p[nii][nnj].append(idx)

                        else:               # ri,rj가 최종 좌표
                            p[r][c].remove(idx)
                            p_loc[idx][2],p_loc[idx][3]=ni,nj
                            p[ni][nj].append(idx)


        print(p_loc)
        for i,j in change_stone:
            p_loc[i][j][1]=False                                    # 다시 돌이 된 애들 풀어주고

        # 이동한 거리 합, 메두사로 인해 돌이 된 전사의 수, 메두사를 공격한 전사의 수
        print(move_dist, mx, attack_m)