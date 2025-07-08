'''
B19237 어른 상어 / 2025-03-17 / 체감 난이도 : 골드 1
소요 시간 : 2시간 20분 / 시도 : 1회

[0] 총평
- 느무 관리할게 많다... 구현 하면서 처음에 구상했던 걸 좀 수정하는 바람에 더 복잡하게 푼 것 같다
합칠 수 있는 단계를 합쳤다면 어땠을까?

[1] 타임라인
1. 문제 이해 & 구상 & 자료구조 정해서 인풋받기 (40분)

2. 구현 (1시간 20분)

3. 디버깅 (20분)
-> 냄새가 0인 걸 빼주지 않음
-> si,sj // ni,nj 오타

[2] 배운점 및 실수한 점
- 처음 풀었을 때는 같은 칸에 여러마리가 있을 때 가장 작은 번호의 상어만 남기는 작업을 따로 처리해줬음
-> 주어진 대로 구현하는 것도 좋지만 합칠 수 있을 땐 합치는게 좋음 ( 합치면 상어맵도 길어지지 않음 )

- 만약 들어가는게 정해져있다면
smell=[[[] for _ in range(N)] for _ in range(N)]
위 보다는 아래처럼 크기를 정해놓고 하는게 좋을 것 같음
smell=[[[0,0] for _ in range(N)] for _ in range(N)]

- 우선순위 관련된 부분도 set으로 다 담을 필요 없이 우선순위 대로 비교하면 됨 (교수님 코드 참조)

- 한 배열에서 수정하는 거 헷갈릴 대 새로운 배열 만들고 바꿔치기한 거 써본 건 좋았음
'''

# 1,2,3,4 - 상,하,좌,우
dic={1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}
N,M,k=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(N)]

# !!!!!!!!!!!!!! 상어맵 -> 상어 번호
shark=[[[] for _ in range(N)] for _ in range(N)]

# 처음에 주어지는 방향
first=[0]+list(map(int,input().split()))

# !!!!!!!!!!!!! 냄새 맵 -> (상어 번호, 몇초 남았는지)
smell=[[[] for _ in range(N)] for _ in range(N)]

# !!!!!!!!!!!!! 상어의 위치를 담는 리스트 -> (상어 위치, 방향)
shark_loc=[[] for _ in range (M+1)]

# 우선순위 맵
priority=[[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]+[[list(map(int,input().split())) for _ in range(4)] for _ in range(M)]

for i in range(N):
    for j in range(N):
        if arr[i][j] !=0:
            shark[i][j].append(arr[i][j])
            shark_loc[arr[i][j]]=[(i,j,first[arr[i][j]])]
time=0

for i in range(1, M + 1):
    x, y = shark_loc[i][0][0], shark_loc[i][0][1]
    smell[x][y].append((i, k))

# ================== 초기상태 해줬구

while time <1000:
    # 1초 지났고
    time += 1
    # ====================
    # 상어 이동하고, 냄새 뿌리고
    # 이미 있는 거에는 1 줄이고 없는 거에는 k만큼 추가하고
    # [2] 모든 상어가 움직이면서 냄새를 뿌릴 거야
    for i in range(1, M + 1):
        # 내가 지금 보고 있는 상어 번호는 i번
        # 그 상어의 현재 위치는 si,sj, 현재 방향은 now_dr
        if shark_loc[i] != []:
            si, sj, now_dr = shark_loc[i][0][0], shark_loc[i][0][1], shark_loc[i][0][2]
            empty = set()
            mine = set()

            for dr in range(1, 5):
                di, dj = dic[dr]
                ni, nj = si + di, sj + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if smell[ni][nj] == []:
                        empty.add(dr)
                    # 여기 좀 비효율적
                    else:
                        for num, tm in smell[ni][nj]:
                            if num == i:
                                mine.add(dr)

            # 우선순위에 따라 골라
            if len(empty) >= 1:
                # shark의 우선 순위에 따라서
                for direction in priority[i][now_dr-1]:
                    if direction in empty:
                        # 그 방향으로 이동할거야
                        ddi, ddj = dic[direction]
                        # shark_loc에 업데이트 해줘야하고, arr에 업데이트 해줘야하고 ( 상어 관련 )
                        fi, fj = si + ddi, sj + ddj
                        shark_loc[i] = [(fi, fj, direction)]
                        shark[si][sj].remove(i)
                        shark[fi][fj].append(i)
                        break
            else:
                for direction in priority[i][now_dr-1]:
                    if direction in mine:
                        # 그 방향으로 이동할거야
                        ddi, ddj = dic[direction]
                        # shark_loc에 업데이트 해줘야하고, arr에 업데이트 해줘야하고 ( 상어 관련 )
                        fi, fj = si + ddi, sj + ddj
                        shark_loc[i] = [(fi, fj, direction)]
                        shark[si][sj].remove(i)
                        shark[fi][fj].append(i)
                        break

    # 한 칸에 여러마리이면 가장 작은 번호 상어 빼고 다 사라진다
    for i in range(N):
        for j in range(N):
            if len(shark[i][j])>1:
                shark[i][j].sort()
                for l in range(1,len(shark[i][j])):
                    shark_loc[shark[i][j][l]]=[]
                shark[i][j]=[shark[i][j][0]]

    # 냄새 관련 ( 원래 있었던 곳에는 -1 씩 해주고, 새로운 칸에는 냄새 넣어야해 )
    # 이제 새로운 위치가 shark_loc에 있을 거임
    new_smell = [[[] for _ in range(N)] for _ in range(N)]

    # 원래 smell에 있던 건 빼줄 거야
    for i in range(N):
        for j in range(N):
            if smell[i][j] != []:
                for num, tm in smell[i][j]:
                    if tm-1 !=0:
                        new_smell[i][j].append((num, tm - 1))

    for i in range(1, M + 1):
        if shark_loc[i] != []:
            x, y = shark_loc[i][0][0], shark_loc[i][0][1]
            new_smell[x][y].append((i, k))

    # 냄새맵 바꿔치기
    smell=new_smell

    # =======================
    # 다 더했을 때 1이면
    tot=0
    for i in range(N):
        for j in range(N):
            if shark[i][j] != []:
                tot+=sum(shark[i][j])
    if tot == 1:
        print(time)
        break
else:
    print(-1)


''' 리팩토링한 코드
N,M,k=map(int,input().split())

# 1,2,3,4 - 상,하,좌,우
dic={1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}

# 상어맵 -> 상어 번호 -> 항상 하나씩만 들어감
shark=[list(map(int,input().split())) for _ in range(N)]

# 처음에 주어지는 방향
first=[0]+list(map(int,input().split()))

# 냄새 맵 -> (상어 번호, 몇초 남았는지)
smell=[[[0,0] for _ in range(N)] for _ in range(N)]

# 상어의 위치를 담는 리스트 -> (상어 위치, 방향)
shark_loc=[[0,0,0] for _ in range (M+1)]

# 우선순위 맵
priority=[[[0]*4,[0]*4,[0]*4,[0]*4]]+[[list(map(int,input().split())) for _ in range(4)] for _ in range(M)]

for i in range(N):
    for j in range(N):
        if shark[i][j] !=0:
            shark_loc[shark[i][j]]=[i,j,first[shark[i][j]]]
time=0

for i in range(1, M + 1):
    x, y = shark_loc[i][0], shark_loc[i][1]
    smell[x][y]=[i,k]

# ================== 초기상태 해줬구
while time < 1000:
    # 1초 지났고
    time += 1
    # ====================
    # 상어 이동하고, 냄새 뿌리고
    # 이미 있는 거에는 1 줄이고 없는 거에는 k만큼 추가하고
    # [2] 모든 상어가 움직이면서 냄새를 뿌릴 거야

    for i in range(1, M + 1):
        # 내가 지금 보고 있는 상어 번호는 i번
        # 그 상어의 현재 위치는 si,sj, 현재 방향은 now_dr
        if shark_loc[i] != [0,0,0]:
            si, sj, now_dr = shark_loc[i][0], shark_loc[i][1], shark_loc[i][2]
            empty = set()
            mine = set()

            for dr in range(1, 5):
                di, dj = dic[dr]
                ni, nj = si + di, sj + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if smell[ni][nj] == [0,0]:
                        empty.add(dr)
                    else:
                        if smell[ni][nj][0] == i:
                            mine.add(dr)

            # 우선순위에 따라 골라
            if len(empty) >= 1:
                # i는 shark의 번호,
                for direction in priority[i][now_dr-1]:
                    if direction in empty:
                        # 그 방향으로 이동할거야
                        ddi, ddj = dic[direction]
                        # shark_loc에 업데이트 해줘야하고, arr에 업데이트 해줘야하고 ( 상어 관련 )
                        fi, fj = si + ddi, sj + ddj
                        shark[si][sj]=0
                        shark_loc[i]=[0,0,0]
                        # 이게 아니면 그냥 없어지니까

                        if shark[fi][fj]==0 or shark[fi][fj]>i:
                            shark_loc[i] = [fi, fj, direction]
                            shark[fi][fj]=i
                        break
            else:
                for direction in priority[i][now_dr-1]:
                    if direction in mine:
                        # 그 방향으로 이동할거야
                        ddi, ddj = dic[direction]
                        # shark_loc에 업데이트 해줘야하고, arr에 업데이트 해줘야하고 ( 상어 관련 )
                        fi, fj = si + ddi, sj + ddj
                        shark[si][sj] = 0
                        shark_loc[i] = [0, 0, 0]
                        # 이게 아니면 그냥 없어지니까

                        if shark[fi][fj] == 0 or shark[fi][fj] > i:
                            shark_loc[i] = [fi, fj, direction]
                            shark[fi][fj] = i
                        break

    # 냄새 관련 ( 원래 있었던 곳에는 -1 씩 해주고, 새로운 칸에는 냄새 넣어야해 )
    # 이제 새로운 위치가 shark_loc에 있을 거임
    new_smell = [[[0,0] for _ in range(N)] for _ in range(N)]

    # 원래 smell에 있던 건 빼줄 거야
    for i in range(N):
        for j in range(N):
            if smell[i][j] != [0,0] and smell[i][j][1]-1 !=0:
                new_smell[i][j]=[smell[i][j][0], smell[i][j][1]- 1]

    for i in range(1, M + 1):
        if shark_loc[i] != [0,0,0]:
            x, y = shark_loc[i][0], shark_loc[i][1]
            new_smell[x][y]=[i,k]

    # 냄새맵 바꿔치기
    smell=new_smell

    # =======================
    # 다 더했을 때 1이면
    if sum(map(sum,shark)) == 1:
        print(time)
        break
else:
    print(-1)

'''