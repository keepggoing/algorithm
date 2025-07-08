''' 2차풀이
[0] 타임라인
구상 (20분)
구현 (30분)
검증 (10분)

[1] 실수한점

[2] 배운점

'''
from collections import deque

def bfs(i, j, num):
    q = deque([(i, j)])
    v[i][j] = num
    pivot = arr[i][j]
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == pivot and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = num
                cnt += 1

    # 다 돌고 나서
    inform[num] = (pivot, cnt)

def next_to(one, two):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == one:
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == two:
                        cnt += 1
    return cnt

def rotate(arr):
    new_arr=list(map(list,zip(*arr)))[::-1]

    for si,sj in ((0,0),(0,half+1),(half+1,0),(half+1,half+1)):
        for i in range(half):
            for j in range(half):
                new_arr[si+i][sj+j]=arr[si+half-1-j][sj+i]

    return new_arr
# ==============================
N=int(input())
half=N//2
arr=[list(map(int,input().split())) for _ in range(N)]
score=0

for _ in range(4):
    inform={}
    v=[[0]*N for _ in range(N)]

    num=1
    for i in range(N):
        for j in range(N):
            if v[i][j]==0:
                bfs(i,j,num)
                num+=1

    # =======
    for i in range(1,num):
        for j in range(i+1,num):
            # i,j 각각에는 visited에 쓰인 수가
            cnt=next_to(i,j)
            score+=(inform[i][1]+inform[j][1])*inform[i][0]*inform[j][0]*cnt
    # ======
    arr=rotate(arr)

print(score)

'''
코드트리 예술성 / 2025-03-21 / 체감 난이도 : 골드 3
소요 시간 : 1시간 50분 / 시도 : 1회

[0] 총평
- 집중력이 확 흐트러지고 나니까 아무것도 못하겠는 스스로를 발견..
주위 환경이나 소음에 영향 받지 말고 문제풀 땐 젭알 문제와 내 풀이 생각만 하자 시험 때도 내가 극복해야할 부분이다

[1] 타임라인
1. 문제 이해 & 구상 (10분)
2. 회전 빼고 구현 (20분)
3. 회전 구현 (2시간)
말도...안돼..

[2] 배운점 및 실수한 점
- 찐 최종으로 회전 정리
1. 그냥 (0,0) 기준으로 좌표 바꾸는 거 완성하고 가중치는 마지막에 양쪽에 si,sj 더해주면 됨
2. new_arr i,j에 arr의 어떤 좌표들이 온 건지 썼지? 그럼 규칙 발견하는 거지
ex) new_arr의 행 인덱스가 그대로 열에 적혀있는 거 발견, 반대로 적혀있는 거 발견
3. zip 썼다가 인덱스 썼다가 왔다갔다 하는 거 너무 시간낭비
일단 인덱스로 밀고 나가기
4. 꼭 맨날 하던 사각형 회전 말고 t자 회전 이런 것도 걍 목적지 기준으로 인덱스 생각하면 뭐든 된다

[3] 시간 복잡도
총 4번 진행할 거고 각각은 bfs,comb,rotate 모두 n**2
900의 상수배

[4] 엣지 케이스
(서현언니의 사고과정 따라하기..)
- 문제에서 주어진 건 다 5x5네? -> 다른 크기 만들어보기
- 가장 큰 거 29x29 만들어서 잘 돌아가는지 돌려보기
- 그룹이 안 정해지는 거
7
1 2 3 4 5 6 7
5 4 1 2 3 7 6
4 1 2 3 5 9 8
2 3 4 5 6 7 2
4 2 1 2 3 4 5
3 4 5 6 7 8 9
1 2 3 4 5 6 7

'''

from collections import deque

def bfs(si, sj, c):
    q = deque([(si, sj)])
    v[si][sj] = c
    pivot=arr[si][sj]
    cnt=1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0 and arr[ni][nj] == pivot:
                q.append((ni, nj))
                v[ni][nj] = c
                cnt+=1
    return cnt

# ========================================================================
def comb(num1,num2):                                              # num1,num2는 영역의 숫자
    cnt=0                                                         # num1의 영역에서 사방에 num2 영역 숫자가 있다면 맞닿은 거 -> cnt+=1
    for i in range(n):
        for j in range(n):
            if v[i][j] == num1:
                pivot1=arr[i][j]
                for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                    ni,nj=i+di,j+dj
                    if 0<=ni<n and 0<=nj<n and v[ni][nj]==num2:
                        pivot2=arr[ni][nj]
                        cnt+=1
    if cnt==0:
        return 0                                                # 맞닿은게 없다면 0
    else:
        return (dic[num1]+dic[num2])*pivot1*pivot2*cnt          # dic에서 영역에 포함된 개수를 뽑아오고, 각 숫자, 맞닿은 변 계산해서 return

# ========================================================================
def rotate():
    global arr
    new_arr = [[0] * n for _ in range(n)]

    for i in range(0,n):
        new_arr[half][i]=arr[i][half]

    for j in range(0,n):
        new_arr[j][half]=arr[half][n-1-j]

    for si,sj in ((0,0),(0,half+1),(half+1,0),(half+1,half+1)):
        for i in range(half):
            for j in range(half):
                new_arr[si+i][sj+j]=arr[si+half-1-j][sj+i]
    arr = [row[:] for row in new_arr]

# ========================================================================

n=int(input())
total=0
half=n//2
arr=[list(map(int,input().split())) for _ in range(n)]

for _ in range(4):
    v=[[0]*n for _ in range(n)]
    c=1
    dic={}
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:                    # bfs를 돌면서 v 배열에 영역 표시
                cnt=bfs(i,j,c)                  # 영역을 표시할 때는 c로 (1부터), bfs 끝날 때마다 c 하나씩 올리는 거
                dic[c]=cnt                      # bfs의 return 값은 그 영역에 몇개있는지? 이고 이를 딕셔너리에 저장해둠
                c+=1

    ans=0
    for num1 in range(1,c):                     # 2개를 뽑아서 comb 함수로 넘길거임
        for num2 in range(num1+1,c):
            ans+=comb(num1, num2)
    total+=ans
    rotate()
print(total)
