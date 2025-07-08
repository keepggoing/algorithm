'''2차 풀이
[0] 타임라인
구상 (45분)
구현 (50분)
검증 및 디버깅 (20분)

[1] 실수한점
1. global 선언 안해줌
-> 코드 중간 중간 검토하다가 오류 뜨면 무조건 적어두기, 같은 실수 여러번 했을 가능성이 높으니까
2. while문에서 break 하나 빼먹음
3. 루돌프 위치 그때 그때 업데이트해서 바꾸면 안 되는데 그렇게 함
4. 함수 이름이랑 같은 변수 이름 쓰면 안됨
5. p_arr에 초기화 하는 거 하나 빼먹음

[2] 배운점
1. 연쇄작용시 temp에다 넣어두고 하나씩 옮기는 방법
def interaction(temp, ni, nj, di, dj):
    global out
    while True:
        if 0 <= ni < N and 0 <= nj < N:
            if p_arr[ni][nj] == 0:
                p_loc[temp][2], p_loc[temp][3] = ni, nj
                p_arr[ni][nj] = temp
                break
            else:
                new_temp = p_arr[ni][nj]
                p_loc[temp][2], p_loc[temp][3] = ni, nj
                p_arr[ni][nj] = temp

                ni, nj = ni + di, nj + dj
                temp = new_temp

        else:  # 범위가 벗어나면 temp는 죽음
            p_loc[temp][1] = 1
            out -= 1
            break
'''

def my_print():
    print('루돌프의 위치')
    print(ri,rj)
    print("====")
    print('산타 위치 모음')
    print(p_loc)
    print("====")
    print('산타맵')
    for row in p_arr:
        print(*row)
    print('====')
    print('산타점수')
    print(p_score)

# N은 격자크기, M은 턴 수, P는 산타 수, C와 D는 추가해야 할 점수
N,M,P,C,D=map(int,input().split())

# 루돌프의 위치
ri,rj=map(lambda x:int(x)-1,input().split())

# 산타 관련된 거
p_loc=[[0,0,0,0] for _ in range(P+1)]
p_arr=[[0]*N for _ in range(N)]
p_score=[0]*(P+1)
out=P

for _ in range(P):
    idx,si,sj=map(int,input().split())
    si,sj=si-1,sj-1
    p_loc[idx]=[0,0,si,sj]
    p_arr[si][sj]=idx

#print('[초기 상태]')
#my_print()
#print('==================')

def dist(si,sj,ei,ej):
    return (si-ei)**2 + (sj-ej)**2

def interaction(temp, ni, nj, di, dj):
    global out
    while True:
        if 0 <= ni < N and 0 <= nj < N:
            if p_arr[ni][nj] == 0:
                p_loc[temp][2], p_loc[temp][3] = ni, nj
                p_arr[ni][nj] = temp
                break
            else:
                new_temp = p_arr[ni][nj]
                p_loc[temp][2], p_loc[temp][3] = ni, nj
                p_arr[ni][nj] = temp

                ni, nj = ni + di, nj + dj
                temp = new_temp

        else:  # 범위가 벗어나면 temp는 죽음
            p_loc[temp][1] = 1
            out -= 1
            break

def collision(ci,cj,santa_idx,score,di,dj,turn):
    global out

    ni,nj=ci+di*score,cj+dj*score
    p_score[santa_idx]+=score

    if ni<0 or ni>=N or nj<0 or nj>=N:
        p_loc[santa_idx][1]=1
        out-=1
        p_arr[ci][cj]=0

    else:
        p_arr[ci][cj] = 0
        if p_arr[ni][nj] == 0:
            p_loc[santa_idx]=[turn+2,0,ni,nj]
            p_arr[ni][nj]=santa_idx
        else:
            temp=p_arr[ni][nj]
            p_loc[santa_idx]=[turn+2,0,ni,nj]
            p_arr[ni][nj]=santa_idx
            # santa_idx가 ni,nj로 가고 싶은데 누가 있는 거야
            # 갈 곳 잃은 산타의 인덱스가 temp에, 갈 곳 잃은 산타가 다음에 갈 곳이 ni,nj에, 사용한 방향이 di,dj에
            interaction(temp,ni+di,nj+dj,di,dj)

# =======================================

for turn in range(1,M+1):

    # P명의 산타가 모두 탈락하면 즉시 게임 종료
    if out == 0:
        break

    # [1] 루돌프의 움직임
    pivot=(-5001,-1,-1)
    for idx in range(1,P+1):
        if p_loc[idx][1]==0:
            _,_,si,sj=p_loc[idx]
            distance=dist(ri,rj,si,sj)
            if (-distance,si,sj)>pivot:
                pivot=(-distance,si,sj)
                choose_santa=idx

    # 이제 choose_santa에는 돌진할 산타의 인덱스가 있고
    # pivot에는 -거리,좌표가 들어가있음
    mn_dist=-pivot[0]
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
        ni,nj=ri+di,rj+dj
        if 0<=ni<N and 0<=nj<N and dist(ni,nj,pivot[1],pivot[2])<mn_dist:
            mn_dist=dist(ni,nj,pivot[1],pivot[2])
            nri,nrj=ni,nj
            rdi,rdj=di,dj

    # 이렇게 되면 nri,nrj가 바뀐 루돌프의 위치가 됨
    ri,rj=nri,nrj
    # rdi,rdj에는 사용한 방향이 들어가있고
    if p_arr[ri][rj] !=0:
        collision(ri,rj,p_arr[ri][rj],C,rdi,rdj,turn)

    #print(turn,'턴 // [1] 루돌프의 움직임 후')
    #my_print()
    #print("================")
    # [2] 산타의 움직임
    for idx in range(1,P+1):
        # 기절하지 않았고, 탈락하지도 않은 산타에 대해서
        if p_loc[idx][0]<=turn and p_loc[idx][1]==0:
            _,_,si,sj=p_loc[idx]
            pivot=dist(ri,rj,si,sj)
            sdi,sdj=0,0
            # 상,우,하,좌 우선순위
            for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
                ni,nj=si+di,sj+dj
                if 0<=ni<N and 0<=nj<N and dist(ri,rj,ni,nj)<pivot and p_arr[ni][nj]==0:
                    pivot=dist(ri,rj,ni,nj)
                    sdi,sdj=di,dj

            # 움직여야 할 때
            if (sdi,sdj) != (0,0):
                p_arr[si][sj]=0
                ni,nj=si+sdi,sj+sdj
                p_arr[ni][nj]=idx
                p_loc[idx][2],p_loc[idx][3]=ni,nj

                if (ri,rj) == (ni,nj):
                    collision(ri,rj,idx,D,-sdi,-sdj,turn)

    # [3] 턴의 마지막에서 아직 탈락하지 않았으면 점수 추가
    for idx in range(1,P+1):
        if p_loc[idx][1] == 0:
            p_score[idx]+=1

    #print(turn,'턴 // [2] 산타의 움직임 & 점수 추가 후')
    #my_print()
    #print("================")

print(*p_score[1:])

'''
[체감 난이도 & 총평]
골 1
손구상에만 집착할 필요 없음 주석으로 정리하는 것도 잘 섞어서 써야함 유도리있게 ㄱㄱ

[시간복잡도]
턴 1000번 x ( 산타 수 최대 30번 x 4번 정도 봄 )

[헷갈렸던 점]
1. 상호작용을 통해 산타가 새로운 곳으로 갔는데 또 루돌프 만나면 어떡해 ..?
-> 상호작용시 사용하는 방향 때문에 다시 루돌프를 마주칠 일 없음
2. 산타가 움직일 때 사용하는 거리가 문제에서 주어진 거리를 말하는 건지 진짜 갈 수 있는 거리를 말하는 건지?
-> 문제에서 주어진 거리임

[타임라인]
1400 - 1430 문제 이해 및 구상
1430 - 1500 루돌프 구현 완료 ( 타자 칠 때 실수 줄이겠다고 천천히 쳤더니 엄청 오래걸림 )
1500 - 1522 구현 중 갑자기 의문이 들어서 stop ( 주의할점 1번 )
1522 - 1535 생각 정리
1535 - 1620 구현 완료
1620 - 1650 디버깅
1650 - 1700 코드 검토 및 검증

[배운점 및 실수한 점]
- 산타 움직일 때 상하좌우에 우선순위 줬다고 해서 거리가 줄자마자 break 했는데 그러면 안됨
-> 일단 최단거리 -> 같다면 상하좌우 우선순위니까 부등호 없이 for문 끝까지 돌면됨
- 누가 움직여서 충돌했냐에 따라 방향 다른데 분기 빼먹음
- 방향 안 바꾸고 넣어줌 (알고 있었는데도 실수함 - 이런 부분은 다버깅할 때도 주의해서 보면 좋을 듯)

[리팩토링 by 갓서현팀장님]
- 원하는 단어 코드에서 계속 찾고 싶으면 Alt J 누르면 됨
- 2로 해서 하나씩 줄일 필요 없고 turn으로 해서 not in 으로 하면 됨
- collision에서도 who로 나누지 말고 C와 D를 매개변수로 보내면 됨

'''

def my_print(turn):
    print(turn)
    print('[1] 산타들의 위치')
    for row in s:
        print(*row)
    print('------')
    print('[2] 산타플래그 정보')
    print(s_flag)
    print('------')
    print('[3] 루돌프 위치')
    print(ri,rj)
    print('------')
    print('[4] 점수')
    print(ans)
    print('========================')

# N은 게임판 크기, M은 턴 수, P는 산타 수, C는 루돌프 힘, D는 산타 힘
N,M,P,C,D=map(int,input().split())

# 루돌프의 위치
ri,rj=map(lambda x: int(x)-1, input().split())

# 산타에 대해서 이렇게 세개로 관리
s=[[0]*N for _ in range(N)]                     # 산타 인덱스 표시
s_loc=[[0,0] for _ in range(P+1)]               # 산타 좌표
s_flag=[[0,0] for _ in range(P+1)]              # 탈락?, 기절? ( 기절은 2,1,0 으로 표시됨 )

for _ in range(P):
    idx,i,j=map(int,input().split())
    i,j=i-1,j-1
    s[i][j]=idx
    s_loc[idx]=[i,j]

# 점수
ans=[0]*(P+1)
# my_print(0)

# ========================================================================================
for turn in range(1,M+1):

    # [1] 루돌프의 움직임 : 가장 가까운 산타 선정
    # [1-1] 산타 골라
    d,r,c=-5000,-1,-1
    for i in range(1,P+1):
        if s_flag[i][0] == 0:           # 탈락하지 않은 산타
            si,sj=s_loc[i]
            dist=(si-ri)**2 + (sj-rj)**2
            if (-dist,si,sj)>(d,r,c):
                d,r,c,idx=-dist,si,sj,i

    d=-d                                # 비교할 때 거리 음수로 했으니까

    # [1-2] 가장 가까워지는 방향 정해
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)):
        ni,nj=ri+di,rj+dj

        # 범위 내이고
        if 0<=ni<N and 0<=nj<N and (ni-r)**2 + (nj-c)**2 < d:
            ei,ej=ni,nj
            d=((ni-r)**2 + (nj-c)**2)
            edi,edj=di,dj

    # 위 for문을 끝내면
    # ei,ej에 루돌프의 위치가, edi,edj에는 방향이
    ri,rj=ei,ej


    # ========================================================================================
    # 산타 - 산타 상호작용

    def interaction(idx,i,j,di,dj):
        temp = [(idx, i, j)]                    # temp에다 움직여야 하는 산타 인덱스, 좌표 넣을거야
        ci, cj = i, j
        while s[ci][cj] != 0:                   # 누가 있다면 계속해서 할 거야
            n_idx = s[ci][cj]
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni >= N or nj < 0 or nj >= N:      # 범위 밖을 나가면 걔는 끝내
                s_flag[n_idx][0] = 1                        # 탈락 플래그 바꿔주고
                break

            temp.append((n_idx, ni, nj))                    # 아니면 temp에 넣고 계속 돌아
            ci, cj = ni, nj

        for idx,x,y in temp:                                # 산타맵 s와 s_loc에 반영
            s[x][y]=idx
            s_loc[idx]=[x,y]


    # ========================================================================================
    # 루돌프 - 산타 충돌

    def collision(who, i, j, di, dj):
        idx = s[i][j]
        s[i][j] = 0                         # 맵에서 원래 위치 없애준다
        ans[idx] += who
        ei, ej = i + di * who, j + dj * who

        # 포물선을 그리고 간 곳이 범위 밖이면
        if ei < 0 or ei >= N or ej < 0 or ej >= N:
            s_flag[idx][0] = 1                  # 탈락 플래그 바꿔주고
        else:
            s_flag[idx][1] = turn                  # 범위 안이면 일단 기절을 시키긴 해야해

            if s[ei][ej] != 0:                  # 산타가 있으면 상호작용 함수로
                interaction(idx, ei, ej, di, dj)

            else:
                s[ei][ej] = idx
                s_loc[idx] = [ei, ej]

    ## ============================================================
    if s[ri][rj] != 0:
        # 루돌프가 움직인 거고, 충돌이 일어나는 좌표,사용된 방향을 넣는다
        collision(C, ri, rj, edi, edj)
    # ==============================================================
    # [2] 산타의 움직임 1번부터 P번까지 순서대로 움직임
    # 즉각적으로 반영해줘야함
    for i in range(1, P + 1):
        # 기절하지 않고 이미 탈락하지도 않은 산타에 대해서
        if s_flag[i][0] == 0 and s_flag[i][1] not in (turn, turn-1):
            si, sj = s_loc[i]
            dist,origin=(si-ri)**2 + (sj-rj)**2, (si-ri)**2 + (sj-rj)**2
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                ni,nj=si+di,sj+dj
                # 범위 내이고 산타도 없으면 움직일 수 있음 -> shortest 거리 찾아보기
                if 0<=ni<N and 0<=nj<N and s[ni][nj] == 0 and (ni-ri)**2 + (nj-rj)**2<dist:
                    dist=(ni-ri)**2 + (nj-rj)**2
                    ei,ej=ni,nj
                    dii,djj=di,dj

            # 다를 때만 움직이는 것
            if dist != origin:
                s[si][sj]=0
                s[ei][ej]=i
                s_loc[i]=[ei,ej]

                if (ei,ej) == (ri,rj):
                    collision(D, ri, rj, -dii, -djj)

    # ==============================================================
    # [7] 만약 P명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임 종료
    flag=False
    for i in range(1,P+1):
        if s_flag[i][0] == 0:
            ans[i]+=1
            flag=True
    if not flag:
        break
    #my_print(turn)

print(*ans[1:])