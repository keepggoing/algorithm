'''2차풀이
[0] 타임라인
구상(20분)
구현(15분)
디버깅(20분)

[1] 실수한점
1. pivot 설정 잘못함
가장 작게 설정해야하는데 음수 비교이니 0이 가장 작은게 아닌데 잘못 생각
2. 오타, defense를 attack이라고 침
3. 또 bfs에서 visited 확인 안 해줌
4. lst에 무조건 넣는게 아니라 경로마다 들고 다녀야 하는데 실수..
그리고 시작점과 끝나는 점도 다 들어가는데 안 들어간다고 생각하고 코드 짬
5. 부서지지 않은 탑 중 1 증가 시키는 조건 누락

[2] 배운점
1. 중간 중간 검증 무조건 하기

'''
# 행 N, 열 M, K번 반복
N,M,K=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
recent=[[0]*M for _ in range(N)]

# ======

from collections import deque

def bfs(si, sj, ei, ej):
    q = deque([(si, sj, [])])
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1

    while q:
        ci, cj, lst = q.popleft()
        if (ci, cj) == (ei, ej):
            return lst

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = (ci + di) % N, (cj + dj) % M
            if arr[ni][nj] > 0 and v[ni][nj]==0:
                q.append((ni, nj, lst+[(ni,nj)]))
                v[ni][nj] = 1
    return []

def end():
    cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0:
                cnt+=1
                if cnt==2:
                    return 0
    if cnt<=1:
        return 1

def my_print(turn):
    print('====',turn,'턴====')
    print('공격자',ai,aj)
    print('공격대상자',bi,bj)
    for row in arr:
        print(*row)

for turn in range(1,K+1):
    attack=(-5001,-1,-1,-1)

    if end():
        break

    for i in range(N):
        for j in range(M):
            if arr[i][j]>0:
                if (-arr[i][j],recent[i][j],i+j,j)>attack:
                    attack=(-arr[i][j],recent[i][j],i+j,j)

    ai,aj=attack[2]-attack[3],attack[3]
    arr[ai][aj]+=(N+M)
    recent[ai][aj]=turn

    defense=(5001,1001,20,20)
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0 and (ai,aj) != (i,j):
                if (-arr[i][j],recent[i][j],i+j,j)<defense:
                    defense=(-arr[i][j],recent[i][j],i+j,j)

    bi,bj=defense[2]-defense[3],defense[3]
    #my_print(turn)
    # =========================
    lst=bfs(ai,aj,bi,bj)
    #print(lst)
    half = arr[ai][aj] // 2
    arr[bi][bj] -= arr[ai][aj]

    if lst:             # 레이저 성공
        lst.pop()
        #print(lst)
        for x,y in lst:
            arr[x][y]-=half

    else:
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
            x,y=(bi+di)%N,(bj+dj)%M
            if (x,y) != (ai,aj):
                arr[x][y]-=half
                lst.append((x,y))

    # ===============
    lst=set(lst)
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0:
                arr[i][j]=0

            else:
                if (i,j) not in lst and (i,j) != (ai,aj) and (i,j) != (bi,bj):
                    arr[i][j]+=1

    #my_print(turn)
print(max(map(max,arr)))

'''
[체감 난이도 & 총평]
골 2
왜이렇게 꼼꼼하지 못한 거니..................................... 다음 문제부터는 진짜 꼼꼼하게
이런 문제에서는 일단 테케 만들기 전에 주어진 오픈테케 반복횟수 늘려서 보는 노력 정도는 해야지 *****
할만하다고 느낄수록 침착해져라 plz...

[시간복잡도]
1000번 반복 100*4 번 정도
10^3 x 10^2 ㄱㅊ

[주의할 점]
- N,M 다르다
- 부서지지 않은 포탑, 즉 0이 아닌 포탑이 1개가 된다면 그 즉시 중지
-> K번 반복하기 전에 중지될 수가 있나? 맨 위에서 확인
- 공격자가 없을 수가 있나?
-> 근데 위에서 1개일 때 멈추니까 ㄱㅊ
- 누구를 기준으로 8방이라는 거임?
-> 아무래도 공격대상이겠지? 맞음
- 행,열 전부다 도넛행성 맞지? 반대편으로 나온다는게
- 포탄 공격할 때 부서진 포탄이란 말은 없음

[타임라인]
9:00 - 9:15 문제 이해 및 구상
9:15 - 10:00 구현 완료 & 오타 때문에 오픈테케 오류
10:00 - 10:30 오류 수정 및 검증 ...
-> 코드 자신있게 짜는 건 좋은데 이거 할 땐 넘 자신있게 보면 안돼... 의심하는 자세
10:30 - 10:35 2번 틀리고 고침
11:45 끝

[배운점 및 실수한점]
- 주의할 점에 잘 써놓고 bi,bj를 ai,aj로 씀
- 공격할 포탑 정할 때 " 공격자를 제외하고 " 조건 안 넣어줌
- if arr[i][j][0] != 0: 이거를 if arr[i][j] != 0:  이렇게씀
코드를 침착하게 읽었거나 포탑이 하나가 되는 경우를 해봤음 됐잖아?
- 8방으로 피해가 퍼질 때 "공격자가 공격 당할지 않는다" 조건 안 넣어줌

[추가 TC]
- 중간에 남은 포탄이 하나만 되는 경우
4 4 8
0 1 4 4
8 0 10 13
8 0 11 26
0 0 0 0


** history는 다른 2차원 배열로 사용하는게 좋지 않을까?
움직일 일이 없으니까 !!!!!!  
'''

from collections import deque

def bfs(si, sj, ei, ej):
    q = deque([(si, sj, [(si,sj)])])
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1

    while q:
        ci, cj, dist = q.popleft()

        if (ci, cj) == (ei, ej):
            return dist

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = (ci + di) % N, (cj + dj) % M
            if arr[ni][nj][0] != 0 and v[ni][nj] == 0:
                tp = dist + [(ni, nj)]
                q.append((ni, nj, tp))
                v[ni][nj] = 1
    return -1

N,M,K=map(int,input().split())

# 포탄 값, 공격한지 얼마나 됐는지? (공격 받은지랑은 상관 x)
arr=[list(map(lambda x:[int(x),0],input().split())) for _ in range(N)]

for k in range(1,K+1):          # K번 반복할 거야
    # [0] 즉 0이 아닌 포탑이 1개가 된다면 그 즉시 중지
    cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j][0] != 0:
                cnt+=1
    if cnt == 1:
        break

    # [1] 공격자를 선정한다
    a,b,c,d=-5001,-1,-1,-1
    for i in range(N):
        for j in range(M):
            # 부서지지 않은 포탑 중에
            if arr[i][j][0] != 0:
                if (-arr[i][j][0],arr[i][j][1],i+j,j)>(a,b,c,d):
                    a,b,c,d=-arr[i][j][0],arr[i][j][1],i+j,j


    # 선정된 공격자의 좌표
    ai,aj=c-d,d
    arr[ai][aj]=[arr[ai][aj][0]+(N+M),k]

    # ====================================================

    # [2] 공격할 포탑 정한다
    # 가장 크게 해야지
    a, b, c, d = 5001, 1001, 21, 21
    for i in range(N):
        for j in range(M):
            # 부서지지 않은 포탑 중에 나도 아니여야댐
            if arr[i][j][0] != 0 and (i,j) != (ai,aj):
                if (-arr[i][j][0], arr[i][j][1], i + j, j) < (a, b, c, d):
                    a, b, c, d = -arr[i][j][0], arr[i][j][1], i + j, j

    # 선정된 공격대상의 좌표
    bi, bj = c - d, d

    # ====================================================

    # 자 이렇게 해서 (ai,aj,bi,bj)에는 공격자의 좌표, 공격 대상의 좌표가 들어있음
    # [3] 레이저 공격을 시도한다
    result=bfs(ai,aj,bi,bj)
    pivot = arr[ai][aj][0]

    if result != -1:  # 레이저 공격 가능
        for i in range(1,len(result)-1):
            x,y=result[i][0],result[i][1]
            arr[x][y][0]-=pivot//2
        arr[bi][bj][0]-=pivot

    else:   # -1이라면 즉, 레이저 공격이 안 된다면
        result=[(ai,aj),(bi,bj)]
        arr[bi][bj][0]-=pivot
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)):
            ni,nj=(bi+di)%N,(bj+dj)%M
            # print(ni,nj)
            if (ni,nj) != (ai,aj):
                arr[ni][nj][0]-=pivot//2
                result.append((ni,nj))

    # ===================================================
    # [4] 0 이하가 된 건 0으로, [5] 무관한 거는 1씩 증가
    result=set(result)
    for i in range(N):
        for j in range(M):
            if arr[i][j][0]<0:
                arr[i][j][0]=0
            if arr[i][j][0] !=0 and (i,j) not in result:
                arr[i][j][0]+=1

mx=-1
for i in range(N):
    for j in range(M):
        if arr[i][j][0]>mx:
            mx=arr[i][j][0]

print(mx)