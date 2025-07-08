''' 2차 풀이
[0] 타임라인
구상 (17분)
구현 (50분)
디버깅 (20분)

[1] 실수한 점
1. pi,pj=i,j 로 해야하는데 pi,pj=20,20 으로 bfs를 시작함
-> bfs 할 때 주의할 점, 시작하는 값도 비교되는지 꼭 확인하기

2. 음수 튜플 비교에서 실수함
-> 음수 튜플 비교할 때 실제 값과 비교시 사용하는 값이 다르니 주의해서 확인하기

-> 모두 체크리스트 추가하기

[2] 배울점
1. 중력 코드 정리하기
def gravity():
    # 모든 열을 볼거야
    for j in range(0,N):
        # 행 밑에서 부터 볼 건데 일단 포인터 처음엔 맨 마지막 가리키고 있을 거야
        pointer=N-1
        for i in range(N-1,-1,-1):
            if arr[i][j] == -1:         # 못 가는 곳이 나와? 그럼 그 위로 포인터를 올려
                pointer=i-1
            elif 0<=arr[i][j]<=M:       # 만약 옮겨야 할게 나왔어
                if pointer != i:        # 포인터랑 가리키는 곳이 다를 때만
                    arr[pointer][j],arr[i][j]=arr[i][j],-2  # 포인터에 지금 내 값 넣고, 원래 내 자리는 빈곳으로
                pointer-=1              # 포인터 하나 올려주고

2. 회전 zip 코드 정리하기
- 90도 회전
arr=list(map(list,zip(*arr[::-1]))

- 반시계 90도 회전
arr=list(map(list,zip(*arr))[::-1]
'''

from collections import deque

# n은 격자의 크기, m은 서로 다른 폭탄의 종류
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

def bfs(i,j):
    pivot=arr[i][j]
    q=deque([(i,j)])
    v[i][j]=1
    lst=[(i,j)]
    red=set()
    pi,pj=-i,j

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                if arr[ni][nj]==0:
                    q.append((ni,nj))
                    v[ni][nj]=1
                    red.add((ni,nj))
                    lst.append((ni,nj))
                elif arr[ni][nj]==pivot:
                    q.append((ni,nj))
                    v[ni][nj]=1
                    lst.append((ni,nj))

                    if (pi,pj)>(-ni,nj):
                        pi,pj=-ni,nj

    for x,y in red:
        v[x][y]=0           # 0은 원상복구

    if len(lst) > 1:
        return lst, (-len(lst),len(red),pi,pj)
    else:
        return [],(-1,-1,-1)

def gravity():
    # 모든 열을 볼거야
    for j in range(0,N):
        # 행 밑에서 부터 볼 건데 일단 포인터 처음엔 맨 마지막 가리키고 있을 거야
        pointer=N-1
        for i in range(N-1,-1,-1):
            if arr[i][j] == -1:         # 만약 돌이 나와? 그럼 그 위로 포인터를 올려
                pointer=i-1
            elif 0<=arr[i][j]<=M:       # 만약 옮겨야 할게 나왔어
                if pointer != i:        # 포인터랑 가리키는 곳이 다를 때만
                    arr[pointer][j],arr[i][j]=arr[i][j],-2  # 포인터에 지금 내 값 넣고, 원래 내 자리는 빈곳으로
                pointer-=1              # 포인터 하나 올려주고
# =================================

score=0
while True:
    v=[[0]*N for _ in range(N)]
    remove=(400,400,20,20)              # 무조건 작아지도록

    for i in range(N):
        for j in range(N):
            # 방문 아직 안 했고, 폭탄일 때
            if v[i][j]==0 and arr[i][j]>0:
                temp,result=bfs(i,j)
                # temp가 있고, result가 더 작다면
                if temp and remove > result:
                    remove=result
                    lst=temp

    if remove == (400,400,20,20):
        break

    else:
        score += len(lst) ** 2
        for i,j in lst:
            arr[i][j]=-2

        gravity()
        arr=list(map(list,zip(*arr)))[::-1]
        gravity()

print(score)

'''
B21609 상어중학교 / 2025-03-14 / 체감 난이도 : 골드 3
소요 시간 : 1시간 40분 / 시도 : 1회

[0] 총평
- "하라는 대로 차근차근 하면 되겠다. 단, 나오는 변수가 많으니까 잘 정리하면서 가자"
- 긴장한 채로 문제를 읽으면 문제가 안 읽힌다
그럴 땐 손으로 차근차근 쓰면서 뜯어가며 문제를 읽자 여기서 시간 좀 걸리는 건 상관없다
타자 치는 것보다 종이에 글씨를 쓰니 긴장도 덜하다
" 이건 이거 말한는 거고, 저건 이거 말하는 거야 ~ " 를 적어놓자

- 회전시킬 때, 중력작용시킬 때 각각 작은 배열을 가지고 확인해보니 디버깅하기 편하다

[1] 타임라인
1. 문제 이해 & 구상 (20분)

2. find_group 함수 구현 (25분) & 디버깅 (5분)
-> 주석 달고 유닛테스트 후 q에 append를 안 한 실수 발견

3. rotate 함수 구상 & 구현 (15분)

4. 중력 함수 구상 & 구현 (15분)

5. 디버깅 (8분)

[2] 배운점 및 실수한 점
- 나눠서 구현하고 유닛테스트 후 문제 없을 때 넘어가자 ( 디버깅하기 편하다 )
- 문제를 처음 보고 30분이 나에겐 정말 중요하다
침착하게 손으로 써가면서 문제를 분석하고 이해하자 대략 방향 잡는데 30분을 max로 두자

- 실수를 아예 안 할 순 없다 내가 이 변수를 왜 쓰는 건지 주석을 달면서 정리하면 실수 발견이 편하다
-> rotate 함수 new_arr = arr 빼먹음
-> 중력 N까지 모든 열 봐야하는데 N-1로 씀
-> cnt가 아니라 alll 로 해야하는데 실수
-> 제곱을 곱해야함

[3] 리팩토링 하면서 알게된 점
if elif 펼쳐서 쓰면 실수하기 좋으니까 ..
튜플은 순서대로 비교해준다 !! 잘 써먹을 수 있겠다
람다는 체화가 안됨 일단 넘어가

'''

from collections import deque

def find_group(i, j):
    q = deque([(i, j)])
    pivot = arr[i][j]
    v = [[0] * N for _ in range(N)]
    v[i][j] = 1

    # 무지개 블록의 개수
    cnt = 1
    standard = (i, j)
    # 총 개수는 in_group의 길이로 하자
    in_group = set()
    in_group.add((i,j))

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and (arr[ni][nj] == pivot or arr[ni][nj] == 0) and v[ni][nj] == 0:
                v[ni][nj] = 1
                in_group.add((ni, nj))
                q.append((ni, nj))
                if arr[ni][nj] == 0:
                    cnt += 1
                if arr[ni][nj] != 0:
                    if ni < standard[0]:
                        standard = (ni, nj)
                    elif ni == standard[0] and nj < standard[1]:
                        standard = (ni, nj)

    # 다 돌고 나서 만약 크기가 2이상이면 return
    if len(in_group) >= 2:
        return len(in_group), cnt, standard[0], standard[1], in_group
    else:
        return -1, -1, -1, -1, -1

def rotate():
    global arr
    new_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[j][N - i - 1]

    arr = new_arr

def gravity():
    for j in range(0, N):
        for i in range(N - 2, -1, -1):
            # 어떤게 중력작용의 대상이 되냐?
            if arr[i][j] != -1 and arr[i][j] != -2:
                while True:
                    if i + 1 >= N or arr[i + 1][j] != -2:
                        break
                    # 빈 곳이면 떨어진다
                    if arr[i + 1][j] == -2:
                        arr[i + 1][j] = arr[i][j]
                        arr[i][j] = -2
                        i = i + 1


# 격자 한 변의 길이, 색상의 개수
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 출력해야하는 점수
ans = 0

while True:
    # [1] 만족하는 블록 그룹을 선정한다
    # 처음 시작할 때 초기화 해준다
    # 전체 길이, 무지개 블록 개수, 기준 블록 행, 기준 블록 열, 전체 들어있는 좌표
    alll = -1
    cnt = 0
    si = 0
    sj = 0
    in_group = set()

    for i in range(N):
        for j in range(N):
            # 그룹 찾을 때 기준점은 일반 블록일 때
            if arr[i][j] != -1 and arr[i][j] != 0 and arr[i][j] != -2:
                A, C, I, J, G = find_group(i, j)

                if A > alll:
                    alll = A
                    cnt = C
                    si = I
                    sj = J
                    in_group = G

                elif A == alll:
                    if C > cnt:
                        alll = A
                        cnt = C
                        si = I
                        sj = J
                        in_group = G

                    elif C == cnt:
                        if I > si:
                            alll = A
                            cnt = C
                            si = I
                            sj = J
                            in_group = G

                        elif I == si:
                            if J > sj:
                                alll = A
                                cnt = C
                                si = I
                                sj = J
                                in_group = G
    # 업데이트가 안 되었으면
    if alll == -1:
        print(ans)
        break

    # [2] 모든 블록을 제거하고 개수만큼 점수를 획득한다
    for i in range(N):
        for j in range(N):
            if (i, j) in in_group:
                arr[i][j] = -2
    ans += (alll**2)

    # 현재 arr에 대해서 중력 작용을 시킨다
    gravity()

    # 반시계 90도 방향 회전을 한다
    rotate()

    # 중력 작용을 시킨다
    gravity()