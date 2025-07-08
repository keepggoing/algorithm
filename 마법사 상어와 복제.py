'''
B23290 마법사 상어와 복제  / 2025-03-19 / 체감 난이도 : 골드 1
소요 시간 : 2시간 / 시도 : 1회

[0] 총평
- 헤매고 있을 땐 무조건 멈춰 !!!!!!!!!!!

[1] 타임라인
1. 문제 이해 & 구상 & 입력 받기 (25분)

2. 물고기 이동 구현 (15분)
-> arr=[[[] for _ in range(4)] for _ in range(4)] 이렇게 해야하는데
arr=[[]*4 for _ in range(4)] 요렇게 해버림

3. 재귀 구현 (55분)
-> 또 재귀에서 길을 잃을 뻔.. [2]에 정리

4. 나머지 구현 (15분)
-> 상어가 움직인 곳에 다 냄새가 표시되는 걸 보고 물고기가 있는 곳에만 냄새 추가 ! if문 빠진 거 발견 ( 요즘 이런 실수 많이함 )

[2] 배운점 및 실수한 점
< 재귀 짤 때 헤맨 거 >
1. 튜플은 불변 자료형이여서 값 추가 못하는데 값 비교하려면 튜플써야지 !!!! 에 꽂혀서 막 추가 해보고 있었음
안 된다는 걸 깨닫고 비교할 때만 튜플로 바꿔서 비교

2. 작으면 갱신하는 거니까 초기 poss를 크게 잡아야 했는데 작게 잡았음

3. mx 갱신하는 코드를 빼먹어서 poss에 아무것도 안 들어감

4. 같은 곳으로 두번 왔을 때 처리해주지 않아서 잘못 카운트 되는 거 발견, 여기서 또 딱 전에꺼만 어떻게 원상복구 해주지..? 혼란 시작
-> 그냥 모조리 전체 복사 하는 거 생각남 ( 어제 해서 ㅋㅋ )
-> 그래서 시간 오래걸림
-> 근데 사실 전체를 다 복사하면서 원상복구 할 필요 없음 왜냐면 직접 배열에 움직이게 만들지 않아도 되자나
그냥 상어가 간 곳 배열을 들고 다니면서 나중에 set으로 만들어서 한번만 먹게 만들면 됨

5. 튜플 비교가 잘못됨, global poss 배열에 new를 복사할 때 poss = new[:] <- 이게 아니라 이렇게 ->poss=new 해서 얕은 복사됐음
리스트 복사할 땐 조심 또 조심 !!!!
poss = new[:]

[3] 시간복잡도 계산
S번 100 번 돌건데 x ( 배열 도는 건 짜잘하게 16으로 몇개 있고 + 배열 복사는 물고기 최대 1000000마리래 )
10^2 x 10^6 이여서 10^8 아슬아슬 ?

배열 복사 -> 요소의 개수만큼이라고 생각하면 된다구 하심 by 준영 프로님
'''

# 몇번 갔는지, new 배열에 방향 번호 추가, 몇 마리 죽었는지 체크, 상어 시작 좌표
def choose(cnt, new, die, si, sj):
    global poss, mx, temp

    if cnt == 3:
        if die > mx:
            mx=die
            poss = new[:]
        elif die == mx:         # 같다면 튜플로 비교
            new=tuple(new)
            poss=tuple(poss)

            if new < poss:
                poss = list(new)
        return

    for i in range(0, 4):       # 네 방향 중에 골라
        di, dj = s_dic[i]
        ni, nj = si + di, sj + dj

        if 0 <= ni < 4 and 0 <= nj < 4:
            new.append(i)
            eat=len(temp[ni][nj])                           # 먹은 거
            temp[ni][nj]=[]                                 # 먹었으니까 비워주고 이 상태 복사해서 저장해둠
            tp=[[lst[:] for lst in row] for row in temp]

            choose(cnt + 1, new, die+eat, ni, nj)
            new.pop()                                        # 원상복구
            temp=[[lst[:] for lst in row] for row in tp]

# ==========================================================

# 물고기의 수, 마법을 연습한 횟수
M,S=map(int,input().split())
arr=[[[] for _ in range(4)] for _ in range(4)]          # 한 곳에 여러마리 들어갈 수 있으니까
smell=[[0]*4 for _ in range(4)]                         # 냄새는 어떤 물고기한테 나왔는지 중요하지 않고 새로 냄새가 생기면 그냥 업데이트 됨

for _ in range(M):
    fx,fy,d=map(int,input().split())
    fx,fy,d=fx-1,fy-1,d-1
    arr[fx][fy].append(d)

dic={0:(0,-1),1:(-1,-1),2:(-1,0),3:(-1,1),4:(0,1),5:(1,1),6:(1,0),7:(1,-1)}     # 물고기 방향
s_dic={0:(-1,0),1:(0,-1),2:(1,0),3:(0,1)}                                       # 상어 방향

shark_i,shark_j=map(int,input().split())
shark_i,shark_j=shark_i-1,shark_j-1

# ==================== 초기 상태 저장해줬고

ans=0
for _ in range(S):
    # [1] 복제 마법을 위해 미리 깊은 복사 해두기
    cpy=[[lst[:] for lst in row] for row in arr]

    # [2] arr에서 모든 물고기 한 칸 이동한다
    new_arr=[[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            # 물고기가 있는 곳에 대해서
            if arr[i][j] != []:
                # 그 안에 있는 숫자가 방향 dr이 됨
                for dr in arr[i][j]:
                    pivot=dr
                    while True:
                        di,dj=dic[dr]
                        ni,nj=i+di,j+dj
                        # 범위 밖이거나, 상어가 있거나, 냄새가 있거나
                        if ni<0 or ni>=4 or nj<0 or nj>=4 or (ni,nj)==(shark_i,shark_j) or smell[ni][nj] != 0:
                            dr=(dr-1)%8 # 방향을 바꾸고 다시 확인

                            if pivot==dr: # 한 바퀴 돌고 같은 방향으로 돌아왔으면 이동 안 하고 그냥 넣어준다
                                new_arr[i][j].append(dr)
                                break
                        else:
                            # 만약 내가 갈 수 있는 곳이면 위치를 넣는다
                            new_arr[ni][nj].append(dr)
                            break

    # 다 이동했으면 상어맵 바꿔치기
    arr=new_arr

    # =================================
    # [3] 상어 움직일 건데 3개를 골라야함
    poss=[4,4,4]
    mx=0
    temp=[[lst[:] for lst in row] for row in arr]  # arr는 남겨두고 temp로만 백트래킹 해봄
    # 이 choose 함수를 통해 poss가 결정되겠지
    choose(0,[],0,shark_i,shark_j)

    # 이제 poss에 가야하는 방향들이 들어있음 poss 대로 움직이면 됨
    # ===================== 냄새를 한 턴에 먼저 줄이고 나서
    for i in range(4):
        for j in range(4):
            if smell[i][j] != 0:        # 0보다 클 때만
                smell[i][j]-=1

    for d in poss:
        di,dj=s_dic[d]
        shark_i,shark_j=shark_i+di,shark_j+dj

        if len(arr[shark_i][shark_j])>0:
            # 빈곳으로 만들고
            arr[shark_i][shark_j]=[]
            # 냄새를 추가해준다 줄어드는 중이였어도 같은 곳에 또 생기면 업데이트 하면 됨
            smell[shark_i][shark_j]=2

    # ==========================
    # [4] 복제 적용된다 !
    for i in range(4):
        for j in range(4):
            if cpy[i][j] != []:
                arr[i][j].extend(cpy[i][j])

for i in range(4):
    for j in range(4):
        if arr[i][j]!=[]:
            ans+=len(arr[i][j])

print(ans)

''' 리팩토링한 코드
def choose(cnt, new, die, si, sj):
    global poss
    global mx
    global temp

    if cnt == 3:
        die=set(die)
        eat=0
        for x,y in die:
            eat+=len(arr[x][y])

        if eat > mx:
            mx=eat
            poss = new[:]
        elif eat == mx:
            new=tuple(new)
            poss=tuple(poss)

            if new < poss:
                poss = list(new)
        return

    for i in range(0, 4):
        di, dj = s_dic[i]
        ni, nj = si + di, sj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            new.append(i)
            die.append((ni,nj))
            choose(cnt + 1, new, die, ni, nj)
            new.pop()
            die.pop()

# ====================== 입력
M,S=map(int,input().split())
arr=[[[] for _ in range(4)] for _ in range(4)]
smell=[[0]*4 for _ in range(4)]

for _ in range(M):
    fx,fy,d=map(int,input().split())
    fx,fy,d=fx-1,fy-1,d-1
    arr[fx][fy].append(d)

dic={0:(0,-1),1:(-1,-1),2:(-1,0),3:(-1,1),4:(0,1),5:(1,1),6:(1,0),7:(1,-1)}
s_dic={0:(-1,0),1:(0,-1),2:(1,0),3:(0,1)}

shark_i,shark_j=map(int,input().split())
shark_i,shark_j=shark_i-1,shark_j-1

# ==================== 초기 상태 저장해줬고
ans=0
for _ in range(S):
    # [1] 복제 마법을 위해 미리 깊은 복사 해두기
    cpy=[[lst[:] for lst in row] for row in arr]

    # [2] arr에서 모든 물고기 한 칸 이동한다
    new_arr=[[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            # 물고기가 있는 곳에 대해서
            if arr[i][j] != []:
                # 그 안에 있는 숫자가 방향 dr이 됨
                for dr in arr[i][j]:
                    pivot=dr
                    while True:
                        di,dj=dic[dr]
                        ni,nj=i+di,j+dj
                        # 범위 밖이거나, 상어가 있거나, 냄새가 있거나
                        if ni<0 or ni>=4 or nj<0 or nj>=4 or (ni,nj)==(shark_i,shark_j) or smell[ni][nj] != 0:
                            dr=(dr-1)%8 # 방향을 바꾸고 다시 확인

                            if pivot==dr: # 한 바퀴 돌고 같은 방향으로 돌아왔으면 이동 안 하고 그냥 넣어준다
                                new_arr[i][j].append(dr)
                                break
                        else:
                            # 만약 내가 갈 수 있는 곳이면 위치를 넣는다
                            new_arr[ni][nj].append(dr)
                            break

    # 다 이동했으면 상어맵 바꿔치기
    arr=new_arr
    # =================================
    # 이제 [2] 상어 움직일 건데 3개를 골라야함
    poss=[4,4,4]
    mx=0
    # 이 choose 함수를 통해 poss가 결정되겠지
    choose(0,[],[],shark_i,shark_j)

    # 이제 poss에 가야하는 방향들이 들어있음 poss 대로 움직이면 됨
    # ===================== 냄새를 한 턴에 먼저 줄이고 나서
    for i in range(4):
        for j in range(4):
            if smell[i][j] != 0:
                smell[i][j]-=1

    for d in poss:
        di,dj=s_dic[d]
        shark_i,shark_j=shark_i+di,shark_j+dj

        # 죽어
        if len(arr[shark_i][shark_j])>0:
            # 빈곳으로 만들고
            arr[shark_i][shark_j]=[]
            # 냄새를 추가해준다 줄어드는 중이였어도 업데이트 하면 됨
            smell[shark_i][shark_j]=2

    for i in range(4):
        for j in range(4):
            if cpy[i][j] != []:
                arr[i][j].extend(cpy[i][j])

for i in range(4):
    for j in range(4):
        if arr[i][j]!=[]:
            ans+=len(arr[i][j])

print(ans)
'''