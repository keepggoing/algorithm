''' 2차 풀이
[실수한 점]
도둑말 위치 바꾼 후 원래 있었던 자리 빈 곳으로 만들어주는 코드 한 줄 누락 -> 로직 검토하며 발견

'''

def my_print():
    print(p_loc)
    print("==========")
    for row in p:
        print(*row)

p_loc=[[0,0,0] for _ in range(17)]
p=[[0]*4 for _ in range(4)]

dic={0:(-1,0),1:(-1,-1),2:(0,-1),3:(1,-1),4:(1,0),5:(1,1),6:(0,1),7:(-1,1)}

for i in range(4):
    lst=list(map(int,input().split()))
    for j in range(0,8,2):
        mal,direction=lst[j],lst[j+1]
        direction-=1
        p_loc[mal]=[i,j//2,direction]
        p[i][j//2]=mal

score=0
mal=p[0][0]
_,_,d=p_loc[mal]

score+=mal
p[0][0]=0               # 0은 술래를 의미
p_loc[mal]=[-1,-1,-1]
p_loc[0]=[0,0,d]

# ===========
def simul(p,p_loc):
    for mal in range(1, 17):
        if p_loc[mal] != [-1, -1, -1]:
            si, sj, d = p_loc[mal]
            sd = d
            di, dj = dic[d]
            ni, nj = si + di, sj + dj

            while True:
                if 0 <= ni < 4 and 0 <= nj < 4 and p[ni][nj] != 0:
                    if p[ni][nj] == -1:                             # 빈칸이면 그냥 넣으면 되고
                        p[ni][nj] = mal
                        p[si][sj] = -1                              # 이거 누락됐었음
                        p_loc[mal] = [ni, nj, d]

                    else:  # 빈칸 아니면 바꿔야함
                        other = p[ni][nj]
                        p_loc[other][0], p_loc[other][1] = si, sj
                        p_loc[mal] = [ni, nj, d]
                        p[si][sj] = other
                        p[ni][nj] = mal
                    break

                else:
                    d = (d + 1) % 8
                    if d == sd:
                        break
                    di, dj = dic[d]
                    ni, nj = si + di, sj + dj

            # my_print()

    # =================== 도둑말 옮기기 끝 !
    si, sj, d = p_loc[0]
    di, dj = dic[d]
    lst = []
    for mul in range(1, 4):
        ni, nj = si + di * mul, sj + dj * mul
        if 0 <= ni < 4 and 0 <= nj < 4 and p[ni][nj] != -1:
            lst.append((ni, nj))
    return p,p_loc,lst

p,p_loc,lst=simul(p,p_loc)

def btk(ans,p,p_loc,lst):
    global score

    if not lst:
        score=max(score,ans)
        return

    for i in range(len(lst)):
        t_p=[row[:] for row in p]
        t_p_loc=[row[:] for row in p_loc]
        si,sj,sd=t_p_loc[0]                         # 현재 술래말 위치
        ni,nj=lst[i]                                # 바꿀 술래말 위치
        catch=t_p[ni][nj]                           # 잡은 도둑말 인덱스
        _,_,d=t_p_loc[catch]                        # 잡은 도둑말의 방향을 가지게 되괴
        t_p_loc[0]=[ni,nj,d]                        # 술래말 p_loc에 반영해주고
        t_p_loc[catch]=[-1,-1,-1]                   # 잡은 도둑말도 p_loc에 반영해주고
        t_p[si][sj]=-1                              # 원래 있었던 곳은 빈 곳으로
        t_p[ni][nj]=0                               # 잡은 곳은 술래로
        t_p,t_p_loc,t_lst=simul(t_p,t_p_loc)        # 그렇게 술래말의 위치가 바뀐 상태로 또 simul을 돌리고 얻은 결과로
        btk(ans+catch,t_p,t_p_loc,t_lst)            # 백트랙킹

btk(score,p,p_loc,lst)

print(score)

'''
B19236 청소년상어 / 2025-03-18 / 체감 난이도 : 골드 1
소요 시간 : 4시간 30분 / 시도 : 1회

[0] 총평
- 입력부터 막히네 ㅜㅜ 새로운 거 해보지 말고 하던대로 안전하게 해라
- 뭔가 에러가 생기거나 오픈테케로 엣지를 발견했을 때 그거만 쏙 고치고 급하게 넘어가면 절대 절대 안됨 !!!!!!!!!!!
헉 틀렸네 -> 고침 이 과정에서 빠르게 고치느라 본질을 못 고쳤을 수도 있고 관련해서 놓친 또다른 엣지가 있을 수도 있음
( 스타트 택시때도 그랬잖아 )
그러니까 문제 푸는 도중에도 꼭 기록 해두고 다시 곱씹으면서 생각해봐야해

[1] 타임라인
1. 문제 이해 및 구상 (25분)

2. 입력 구현 (35분)
-> 와우.. zip, extend 등 한 번에 내가 원하는대로 (배열에 두개씩 잘라서 튜플로 넣어주는 거) 만들어주는게 있을 거라고
생각하면서 이것저것 해보다가 시간이 이렇게 흘렀음
이런짓은 하지말자.. 4개를 한 리스트에 쭉 받는 거 어떻게 하지..? 생각했는데 그냥 for문으로 돌리면서 그때 그떄 처리하면 되잖아

3. 물고기 이동 구현 (13분)
-> 방향이 0이 나오는 에러 (디버깅 8분) - 디버깅 너무 오래했고 여기서 빨리 고치느라 잘못 고침
-> 유닛 테스트 하면서 (0,0)에 있는 물고기 fish_loc에 반영 안 한거 , fish_loc에서 물고기가 없어졌으면
안 보는 if문 누락 발견 (10분)
( 아예 물고기가 없으면 안 보는 if문 다른 문제에서도 누락했었음 )

4. 재귀 구현 및 꼬이기 시작 (1시간 10분)
-> 바로 아래 [2]에서 재귀 헤맨 거 정리
이것저것 막 바꾸다보면 시간 진짜 금방 감 ! 헷갈리는 건 무조건 종이에 손으로 써. 그리고 정리해나가
한번 노트북에 손 대고 나서는 뗴기 쉽지 않은데 무조건 멈춰서 헷갈리는 거 정리하고 가야해 특히 재귀에서

[2] 배운점 및 실수한 점
< 재귀 꼬인 이유 >
1) 상어만 원상 복구하면 된다고 생각했음
이번 문제에서는 물고기가 다 이동한 특정 상태에서 상어가 일로가고, 절로 가고 이걸 다 해보고 싶은 거였음
그렇다면 물고기가 다 이동한 특정 상태를 기록해줘야하는데 ?
이걸 어떻게 해..? 생각하면서 상어만 원상복구 해줬음

상어의 위치에 따라 가지치기를 한 거지만은 상어 위치 옮기고 나서 ( 가지 타고 다음 재귀로 가고 나서 ) 물고기 위치도 바뀌니까
전체 맵을 원상복구를 해줘야함 ( 물고기도 이동하기 전 상태로 )

2) 또 헷갈렸던게 score은 매개변수로 들고다니니까 일회용이여서 원상복구를 해줄 필요가 없는건데
어떤 건 원상복구 해줘야하고 어떤 건 안 해도 되고.. 뭔 차이지? 생각 들면서 꼬임
당연한 건데 재귀 코드짜면서 생각 꼬인적 많은 듯 -> 손으로 트리를 그리거나 머릿속에 드는 복잡한 생각들을 말로 적어 말로.. 그리고 정리해 나가

배열이나 전역변수는 그 함수 안에서만 사용하는게 아니니까 원상복구를 해줘야하는 거임

< etc >
- 처음에 입력 받는 거에서도 버벅거림
-> 이럴 떈 바효율적인 방법이여도 괜찮으니 일단 치고 for문으로 돌릴 수 있는게 있나 확인하기

- 점수를 더할 때 score+=prev_n 코드도 위에서 쓰고 함수 호출할 때 매개변수에도 더했음
즉 덧셈이 두번이었음

- 1~8 만큼의 방향만 갖고있어 그래서 8 다음에 1이 나와 -> %8이 아니라 %9로 해줬어야
마지막 수가 어떻게 되는지 집중해서 보면 됨 !!!!

- 3차원 복사하는 법 한번 더 체크 ! arr=[[lst[:] for lst in row] for row in t_arr]
arr=[lst[:] for lst in row for row in t_arr] <- 처음에 이렇게 써서 오류

- 이전에 상어 있던 곳을 [0,0]으로 해주는 코드가 없었음

- 원상복구를 위해 미리 맵 복사해주는 건 poss 전에서 해줘도 됨 그떄 그때 복사할 필요 없음
어차피 가지 뻗기 전 상태는 똑같으니까 ( 거기서 여러 개가 뻗어져 나온 거니까 ! )

'''

def solve(shark_i,shark_j,shark_dr,score):
    global ans

    # 상어가 들어간 곳에 있는 물고기 번호
    prev_n, prev_dr = arr[shark_i][shark_j]
    # -1은 shark가 있음을 뜻함
    arr[shark_i][shark_j] = [-1, shark_dr]
    # 물고기 사라짐
    fish_loc[prev_n] = [100, 100]
    score += prev_n

# ========================

    for i in range(1, len(fish_loc)):
        if fish_loc[i] != [100, 100]: # 물고기가 있다면
            # 초기 위치고
            si, sj = fish_loc[i]
            # 초기 방향이고
            dr = pivot = arr[si][sj][1]
            di, dj = dic[dr]
            ni, nj = si + di, sj + dj

            while True:
                # 격자를 나갔고 상어이면
                if ni < 0 or ni >= 4 or nj < 0 or nj >= 4 or arr[ni][nj][0] == -1:
                    dr = (dr + 1) % 9
                    if dr == 0:
                        dr = 1
                    # 방향이 처음이랑 똑같아지면 자리 못 바꾸고 끝내는 거
                    if dr == pivot:
                        break
                    di, dj = dic[dr]
                    ni, nj = si + di, sj + dj

                else:
                    # 서로 바꿔치기 한 담에 break !
                    change_i, change_dr = arr[ni][nj]
                    # 현재 내 위치에는 ni,nj를 넣어주고
                    arr[si][sj] = [change_i, change_dr]
                    fish_loc[change_i] = [si, sj]

                    arr[ni][nj] = [i, dr]
                    fish_loc[i] = [ni, nj]
                    break

# ============================
    possible = []
    for mul in (1, 2, 3):
        pi, pj = shark_i + dic[shark_dr][0] * mul, shark_j + dic[shark_dr][1] * mul
        if pi < 0 or pi >= 4 or pj < 0 or pj >= 4:
            break
        else:
            if arr[pi][pj][0] != 0: # 빈 곳이 아니면
                possible.append((pi, pj))

    # 가능한 곳이 없으면 전역변수 ans와 비교
    # score은 일회용
    if not possible:
        ans=max(ans,score)
        return

    t_arr=[[lst[:] for lst in row] for row in arr]
    t_fish_loc=[row[:] for row in fish_loc]

    # possible 중에서 상어 위치 골라서 갈 거야
    for i,j in possible:
        arr[shark_i][shark_j]=[0,0]

        solve(i,j,arr[i][j][1],score)

        arr=[[lst[:] for lst in row] for row in t_arr]
        fish_loc=[row[:] for row in t_fish_loc]

# ========================

dic={1:(-1,0), 2:(-1,-1), 3:(0,-1), 4:(1,-1), 5:(1,0), 6:(1,1), 7:(0,1), 8:(-1,1)}
# fish_loc에는 i번째 인덱스에 i번째 물고기의 좌표를 적어주는 거고
fish_loc=[[0,0] for _ in range(17)]
# arr에는 (번호,방향)이 적혀있고
arr=[[[0,0] for _ in range(4)] for _ in range(4)]

for i in range(4):
    lst=list(map(int,input().split()))
    for j in range(4):
        arr[i][j]=[lst[j*2],lst[j*2+1]]
        fish_loc[lst[j*2]]=[i,j]

# =======================
ans=0
# 상어 x좌표, y좌표, 상어 방향, 점수 합계
solve(0,0,arr[0][0][1],0)
print(ans)