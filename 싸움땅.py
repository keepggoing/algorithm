'''
p_loc[my_idx][0],p_loc[my_idx][1]=si,sj
이걸 빼먹음
'''

def my_print():
    print(turn,'턴')
    print()
    print('총 맵')
    for row in arr:
        print(*row)
    print()
    print('사람맵')
    for row in p_arr:
        print(*row)
    print()
    print('사람 정보')
    print(p_loc)
    print()
    print('점수')
    print(p_score)
    print("=================")

# N은 격자 크기, M은 플레이어 수, K는 라운드 수
N,M,K=map(int,input().split())
temp=[list(map(int,input().split())) for _ in range(N)]
arr=[[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if temp[i][j] != 0:
            arr[i][j].append(temp[i][j])

p_arr=[[0]*N for _ in range(N)]
p_loc=[[0,0,0,0,0] for _ in range(M+1)]
p_score=[0]*(M+1)

for idx in range(1,M+1):
    x,y,d,power=map(int,input().split())
    x,y=x-1,y-1
    p_loc[idx]=[x,y,d,power,0]
    p_arr[x][y]=idx

# 상 우 하 좌
dic={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}

# =====================================================
for turn in range(1,K+1):

    # 첫번째 플레이어부터 방향대로 한 칸 이동
    for my_idx in range(1,M+1):
        si,sj,d,power,gun=p_loc[my_idx]
        di,dj=dic[d]
        ni,nj=si+di,sj+dj

        if ni<0 or ni>=N or nj<0 or nj>=N:
            d=(d+2)%4
            p_loc[my_idx][2]=d          # 바뀐 방향 넣어놓는다
            di,dj=dic[d]
            ni,nj=si+di,sj+dj


        if p_arr[ni][nj]==0:            # 만약 플레이어가 없다면
            if arr[ni][nj]!=[]:         # 총이 있다면
                if gun != 0:            # 나에게도 총이 있었다면
                    new_gun=max(gun,max(arr[ni][nj]))
                    if new_gun != gun:  # 원래 내꺼랑 다르다면 바꿔야겠지
                        p_loc[my_idx][4]=new_gun
                        arr[ni][nj].remove(new_gun)
                        arr[ni][nj].append(gun)
                else:
                    new_gun=max(arr[ni][nj])
                    p_loc[my_idx][4]=new_gun
                    arr[ni][nj].remove(new_gun)

            p_loc[my_idx][0],p_loc[my_idx][1]=ni,nj
            p_arr[si][sj]=0
            p_arr[ni][nj]=my_idx

        else:                           # 만약 플레이어가 있다면
            other_idx=p_arr[ni][nj]     # 다른 플레이어의 인덱스는 other_idx에
            _,_,o_d,o_power,o_gun=p_loc[other_idx]

            p_arr[si][sj]=0             # 원래 내 위치는 일단 0으로 바꿔놓고
            si,sj=ni,nj                 # 내 위치는 si,sj지

                                                        # 맵에는 내 인덱스만 없는 거야
            if (o_power+o_gun,o_power)>(power+gun,power):   # other_idx가 이겼어, my_idx가 졌어
                p_score[other_idx]+=(o_power+o_gun)-(power+gun)

                if gun != 0:
                    arr[si][sj].append(gun)

                while True:
                    di,dj=dic[d]
                    sni,snj=si+di,sj+dj

                    if sni<0 or sni>=N or snj<0 or snj>=N or p_arr[sni][snj]!=0:
                        d=(d+1)%4
                    else:
                        # 나의 최종 위치는 sni,snj, 방향은 d, 만약 그 위치에 총이 있다면 획득
                        if arr[sni][snj]!=[]:
                            new_gun=max(arr[sni][snj])
                            arr[sni][snj].remove(new_gun)
                        else:
                            new_gun=0
                        p_loc[my_idx]=[sni,snj,d,power,new_gun]
                        p_arr[sni][snj]=my_idx
                        break

                # 이긴 사람처리
                if arr[ni][nj] != []:
                    new_gun=max(arr[ni][nj])
                    if o_gun < new_gun:
                        p_loc[other_idx][4]=new_gun
                        arr[ni][nj].remove(new_gun)
                        arr[ni][nj].append(o_gun)

            else:                                           # my_idx가 이겼어, other_idx가 졌어
                p_score[my_idx] += (power + gun)-(o_power + o_gun)

                # si,sj,ni,nj 모두 싸운 좌표가 들어가있고

                if o_gun != 0:
                    arr[ni][nj].append(o_gun)

                while True:
                    di, dj = dic[o_d]
                    oni, onj = ni + di, nj + dj
                    if oni < 0 or oni >= N or onj < 0 or onj >= N or p_arr[oni][onj] != 0:
                        o_d = (o_d + 1) % 4
                    else:
                        # other의 최종 위치는 oni,onj, 방향은 o_d, 만약 그 위치에 총이 있다면 획득
                        if arr[oni][onj] != []:
                            new_gun = max(arr[oni][onj])
                            arr[oni][onj].remove(new_gun)
                        else:
                            new_gun = 0
                        p_loc[other_idx] = [oni, onj, o_d, o_power, new_gun]
                        p_arr[oni][onj] = other_idx
                        break

                # 이긴 사람처리
                p_arr[si][sj]=my_idx
                p_loc[my_idx][0],p_loc[my_idx][1]=si,sj
                if arr[si][sj]!=[]:
                    new_gun = max(arr[si][sj])
                    if gun < new_gun:
                        p_loc[my_idx][4] = new_gun
                        arr[si][sj].remove(new_gun)
                        arr[si][sj].append(gun)
    #my_print()

print(*p_score[1:])


'''
[체감 난이도 & 총평]
골 1
관리해야할게 많고 로직이 헷갈려서 실수하기 쉽겠다고 생각하면서 품
아니나 다를까 실수가 많았고 그래서 디버깅이 오래걸림

내가 꼼꼼하지 못한 이유가 정보를 선별해서 필요한 걸 손구상에 적어야 하는데
어떤 건 적고 어떤 건 안 적음 뭐가 조심해야할 부분인지 강약조절 하면서 읽어야 하는데 그게 안 되고 있는 듯..

손구상을 좀 제대로 활용해봐라.. n차 풀이하면서 루틴 완벽히 잡자
3시간씩 오래 걸린 문제들 특징은 1. 문제 풀다가 구상이 바꼈거나, 2. 구상이 완벽하지 않아서 스스로 헷갈린 거

하 맨날 같은 결론이다
** 손구상 깔끔하게 하고, 단계별 검증은 필수 **

[시간복잡도]
k x m x n^2 6000000 rㅊ
[타임라인]
0900 - 0930 입력받기 & 구상 완료
0930 - 1014 구현 완료
1014 - 1130 디버깅 후 제출 -> 시간 초과
1130 - 1140 재디버깅

[배운점 및 실수한 점]
- di,dj 따로 안 만들고 dic[dr]로 더해버림
- 복붙 하면서 수정 제대로 안 해서 점수 추가해줄 때 오타 있었음 (o_p + o_w,o_p) - (p + w)
- py_loc[i]=[ni,nj,dr,p,w] 이렇게 리스트로 감싸야 하는데 py_loc[i]=ni,nj,dr,p,w 안 감싸고 있었음
- reverse=True 처리 안 해준 거 다수..
- 변수 잘못 쓴 거 다수..
- 시간 초과난 이유는 상대방이 이긴 경우 계속 ni,nj로 관리하는데 잘못 바꿨을 경우에 원상복구 안 해줌

-> 아무튼 이 모든 실수의 요인은 중간 중간 검증 안 했기 때문임
'''

dic={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}

# n은 격자의 크기, m은 플레이어 수, k는 라운드 수
n,m,k=map(int,input().split())

# 이건 총의 맵
arr=[list(map(lambda x: [int(x)],input().split())) for _ in range(n)]

py=[[0]*n for _ in range(n)]
# 인덱스로 관리하면 되고 // 순서대로 x좌표, y좌표, 방향, 능력치, 총
py_loc=[[0,0,0,0,0] for _ in range(m+1)]

for i in range(1,m+1):
    x,y,d,s=map(int,input().split())
    x,y=x-1,y-1
    py[x][y]=i
    py_loc[i]=[x,y,d,s,0]

# 인덱스 1부터 출력해야함
ans=[0]*(m+1)

# =======================================================
for round in range(1,k+1):                       # k번 라운드를 볼거고
    for i in range(1,m+1):               # 플레이어 인덱스를 i로 하고 한명씩 볼거야
        si,sj,dr,p,w=py_loc[i]           # 초기위치, 초기방향, 초기능력치, 초기 총 공격력
        di,dj=dic[dr]
        ni,nj=si+di,sj+dj    # 한 칸 간다
        if ni<0 or ni>=n or nj<0 or nj>=n:      # 범위 밖이면
            dr=(dr+2)%4                         # 방향 바꾸고
            di, dj = dic[dr]
            ni,nj=si+di,sj+dj                   # 이동한다

        # ===============================
        # 일단 바로 비워줘야해 py에는
        py[si][sj]=0
        # 이제 위치가 ni,nj로 바꼈어 플레이어 있냐 없냐로 우선 구분
        if py[ni][nj] == 0:                 # 플레이어 없으면
            if arr[ni][nj] != []:           # 뭔가 비교해야할게 있어
                if arr[ni][nj][0]>w:
                    if w == 0:
                        w=arr[ni][nj][0]
                        arr[ni][nj].pop(0)

                    else:
                        arr[ni][nj][0],w = w, arr[ni][nj][0]
                        arr[ni][nj].sort(reverse=True)

            # 이제 내꺼에 반영 시키기
            # arr은 할 거 없고
            py[si][sj]=0
            py[ni][nj]=i
            py_loc[i]=[ni,nj,dr,p,w]

        # ============================================================
        # 플레이어가 있다면 싸워야해
        else:
            # ni,nj랑 o_i,o_j랑 같아
            # 기존 사람 인덱스는 i, 상대방은 o_index
            o_index=py[ni][nj]
            o_i,o_j,o_dr,o_p,o_w = py_loc[o_index]

            if (p+w,p)>(o_p+o_w,o_p):               # 지금 보고 있던 플레이어가 이긴다면
                ans[i]+=(p+w)-(o_p+o_w)             # 점수 추가해주고

                # 진 플레이어가 해야할 일
                if o_w != 0:
                    arr[o_i][o_j].append(o_w)       # 본인이 가지고 있는 총을 내려놔
                    arr[o_i][o_j].sort(reverse=True)
                    o_w=0                           # 본인은 총 없어 현재

                while True:
                    o_di, o_dj = dic[o_dr]
                    o_ni, o_nj = o_i + o_di, o_j + o_dj  # 이동을 해
                    if 0<=o_ni<n and 0<=o_nj<n and py[o_ni][o_nj]==0:
                        # 이제 그 사람 위치는 o_ni,o_nj가 되는 거고 총 없는 상태였으니까 그냥 얻기만 하면 됨
                        if arr[o_ni][o_nj] !=[]:
                            o_w=arr[o_ni][o_nj][0]
                            arr[o_ni][o_nj].pop(0)
                        break
                    else:
                        o_dr=(o_dr+1)%4

                # 이긴 플레이어가 해야할 일
                if arr[ni][nj] != []:  # 뭔가 비교해야할게 있어
                    if arr[ni][nj][0] > w:
                        if w == 0:
                            w = arr[ni][nj][0]
                            arr[ni][nj].pop(0)

                        else:
                            arr[ni][nj][0], w = w, arr[ni][nj][0]
                            arr[ni][nj].sort(reverse=True)

                # 다 반영해주기
                # 먼저 py맵
                py[si][sj] = 0
                py[ni][nj]=i        # 기존 값 그냥 없애버림
                py[o_ni][o_nj]=o_index

                # 그다음 py_loc
                py_loc[i]=[ni,nj,dr,p,w]
                py_loc[o_index]=[o_ni,o_nj,o_dr,o_p,o_w]

            # 상대방이 이겼다면
            else:
                ans[o_index] += (o_p + o_w) - (p + w)   # 점수 추가해주고

                # 진 플레이어가 해야할 일
                if w != 0:
                    arr[ni][nj].append(w)  # 본인이 가지고 있는 총을 내려놔
                    arr[ni][nj].sort(reverse=True)
                    w = 0  # 본인은 총 없어 현재

                while True:
                    di, dj = dic[dr]
                    ni, nj = ni + di, nj + dj  # 이동을 해
                    if 0 <= ni < n and 0 <= nj < n and py[ni][nj] == 0:
                        if arr[ni][nj] !=[]:
                            w = arr[ni][nj][0]
                            arr[ni][nj].pop(0)
                        break
                    else:
                        ni,nj=ni-di,nj-dj
                        dr = (dr + 1) % 4

                # 이긴 플레이어가 해야할 일
                if arr[o_i][o_j] != []:  # 뭔가 비교해야할게 있어
                    if arr[o_i][o_j][0] > o_w:
                        if o_w == 0:
                            o_w = arr[o_i][o_j][0]
                            arr[o_i][o_j].pop(0)

                        else:
                            arr[o_i][o_j][0], o_w = o_w, arr[o_i][o_j][0]
                            arr[o_i][o_j].sort(reverse=True)

                # 다 반영해주기
                # 먼저 py맵
                py[si][sj] = 0
                py[ni][nj] = i  # 기존 값 그냥 없애버림

                # 그다음 py_loc
                py_loc[i] = [ni, nj, dr, p, w]
                py_loc[o_index] = [o_i, o_j, o_dr, o_p, o_w]            # 이긴 플레이어는 안 움직이니까

print(*ans[1:])