'''미세먼지 안녕! (1/81) / 20250226 / 체감 난이도 : 골드 4-5
소요 시간 : 1시간 20분 / 시도 : 1회 / 실행 시간 : 364ms / 메모리 : 123232KB

[타임라인]
1. 문제 이해 및 첫번째 함수 구상 (12분)
2. 첫번째 함수 구현 완료 (8분)
3. 첫번째 함수 디버깅 (20분...)
4. 두번째 & 세번째 함수 구상 (7분)
5. 두번째 & 세번째 함수 구현 완료 (18분)
6. 디버깅 (5분)
7. 코드 정리 및 마지막 체크 (5분)

[디버깅 내역]
1. ci,cj 를 i,j로 썼음 ㅋㅋ
2. 기껏 amount를 같이 큐에 넣어주면서 처음 값 유지 하자고 구상했는데 코드엔 amount 안쓰고 arr[ci][cj]로 씀
구상시 sudo code를 잘못 써두니 이런 고생을 ..
이 실수로 디버깅을 20분이나 하고 심장이 빨리 뛰기 시작..
3. 함수 짜고 확인하고 함수 짜고 확인하고 하다 보니
전체 시간 while 문을 안 돌리는 실수를 .. (1초만 한 것)
그래도 이 실수는 바로 발견

[구상]
첫번째 함수 구상 - bfs를 써야겠고 조심해야하는 건 큐에 한 번에 넣어야겠다
그리고 미세먼지 양을 초기값으로 해야하니까 큐에 같이 넣어야겠다
(이렇게 생각해놓고도 잘못씀) -> 무조건 구상하고 sudo code 쓸 때 써둬야 한다

두번째 함수 구상 - 처음엔 인덱스로 회전을 시키고 싶었는데 첫번째 함수 디버깅 오래 하고 나니까 머리가 안 돌아감
그래서 모든 숫자를 temp에 넣어두고 하나씩 가면서 다시 넣어주자고 생각함 ( 좋은 구상은 아닌듯 )

[구현]
이 문제에서 여전히 구상을 완벽하게 안 하고 넘어감
왜 도대체 왜... 구상 완벽하게 안 하면 무조건 구현에서 문제 생긴다 제발 다음엔 그러지 말자

[마지막 체크 포인트]
회전할 때 마지막 칸이 버려지는게 (공기청정기로 들어가는게) 잘 되는지 확인함
while 문 조건 달 때 time<T인지, time<=T 인지 한 번 더 생각

[후기]
자꾸 구상에 통째로 많은 시간을 들이는데 불안해 함 -> 구상을 단계별로 나눠서 했음
첫번째 함수에서 디버깅에 생각보다 많은 시간을 쓰니까 멘탈이 조금 흔들림
그러다보니 두번째 구상할 때 좀 무식하고 안전한 방법으로 구상하게 됨
이게 괜찮은건가..? 한 번에 구상하는 연습도 해야할 듯

그리고 여전히 내 문제는 반례를 안 만들고 못 만든다
제출 전에 꼭 반례 만드는 연습을 할 것
'''

from collections import deque

# [1] 미세먼지 확산시키기
def bfs():
    while q:
        ci,cj,amount=q.popleft()
        # ** 여기서 처음에 amount로 안 하고 arr[ci][cj]로 해서 디버깅 후 발견
        spread = amount // 5
        cnt = 0
        # 네 방향 탐색
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=ci+di, cj+dj
            # 범위 내이고 공청이 아니면 더하고 cnt도 1 추가
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] != -1:
                arr[ni][nj] += spread
                cnt+=1
        arr[ci][cj]-=spread*cnt

# [2] 공기청정기 위 회전
def up_spread(ui,uj):
    temp = [0]
    # 상 하 좌 우
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 시작은 우
    dr = 3
    si, sj = ui, uj

    # temp에 다 공청 바로 위까지 다 들어감
    while True:
        ni, nj = si + dir[dr][0], sj + dir[dr][1]
        if ni==ui and nj==uj:
            break
        if 0 <= ni < N and 0 <= nj < M:
            temp.append(arr[ni][nj])
            si, sj = ni, nj
        else:
            # 상일때 좌 2, 하일때 -, 좌일때 1, 우일때
            dr = [2, 3, 1, 0][dr]

    dr = 3
    si, sj = ui, uj
    num=0

    while True:
        ni, nj = si + dir[dr][0], sj + dir[dr][1]
        if ni==ui and nj==uj:
            break
        if 0 <= ni < N and 0 <= nj < M:
            arr[ni][nj]=temp[num]
            si, sj = ni, nj
            num+=1
        else:
            # 상일때 좌 2, 하일때 -, 좌일때1, 우일때
            dr = [2, 3, 1, 0][dr]

def down_spread(di,dj):
    temp = [0]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dr = 3
    si, sj = di, dj

    while True:
        ni, nj = si + dir[dr][0], sj + dir[dr][1]
        if ni == di and nj == dj:
            break
        if 0 <= ni < N and 0 <= nj < M:
            temp.append(arr[ni][nj])
            si, sj = ni, nj
        else:
            # 상일때 _, 하일때 2, 좌일때 0, 우1일때
            dr = [3,2,0,1][dr]

    dr = 3
    si, sj = di, dj
    num = 0

    while True:
        ni, nj = si + dir[dr][0], sj + dir[dr][1]
        if ni == di and nj == dj:
            break
        if 0 <= ni < N and 0 <= nj < M:
            arr[ni][nj] = temp[num]
            si, sj = ni, nj
            num += 1
        else:
            # 상일때 좌 2, 하일때 -, 좌일때1, 우일때
            dr = [3,2,0,1][dr]

# 입력 받기
N,M,T=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
time=0

# 0초로 시작해서 한 바퀴 돌고 1초
while time<T:
    q=deque()

    # 한 번에 다 넣는다
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and arr[i][j] != -1:
                # 위치, 양 해서 q에 넣고 한 번에 bfs 돌린다
                q.append((i,j,arr[i][j]))
    bfs()

    where=[]

    # 행 쭉 보면서 좌표를 찾기
    for i in range(N):
        if arr[i][0]==-1:
            where.append((i,0))

    ui,uj=where[0][0],where[0][1]
    di,dj=where[1][0],where[1][1]

    # 위에 회전
    up_spread(ui,uj)
    # 아래 회전
    down_spread(di,dj)
    time+=1

# 정답 구하기
ans=0
for i in range(N):
    for j in range(M):
        if arr[i][j] != -1 and arr[i][j] !=0:
            ans += arr[i][j]
print(ans)