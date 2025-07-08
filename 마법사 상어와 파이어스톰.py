''' 2차 풀이
[0] 타임라인
구상 (30분)
구현 (30분)
디버깅 (20분)

[1] 실수한점
1. 깊은 복사, 얕은 복사
-> 체크리스트 추가하기
그때 그때 new_arr을 만들어주는 건 맞지만 arr = new_arr 이렇게 연결하고 아래에서 두 배열을 동시진행 처리할 때 사용하고 있었음
그러면 당연히 new_arr이 바뀔 때 arr도 같이 바뀜

2. 또 >0일때만 하는 건데 if문 안 걸어줌, 이 실수 꽤 많이 함

3. l==0 일 때 continue로 올려버림
이 경우엔 회전만 안 하고 녹이는 건 했어야 함
-> continue 쓸 때 아래 동작 다 안 하는 건지 다시 한번 생각하기

[2] 배운점
1. 인덱스 회전 최종 정리

for si in range(0,N,l):
    for sj in range(0,N,l):
        for i in range(l):
            for j in range(l):
                - 90도 회전
                new_arr[si+i][sj+j]=arr[si+l-1-j][sj+i]

                - 180도 회전
                new_arr[si+i][sj+j]=arr[si+l-1-i][sj+l-1-j]

                - 270도 회전 (반시계 90도)
                new_arr[si+i][sj+j]=arr[si+j][sj+l-1-i]

2. 격자를 자체를 회전하는게 아니라 격자에서 또 4등분 해서 시계 방향 회전

for si in range(0,N,l):
    for sj in range(0,N,l):
        for i in range(half):
            for j in range(half):   # 3 -> 1
                new_arr[si+i][sj+j]=arr[si+i+half][sj+j]
            for j in range(half,l): # 1 -> 2
                new_arr[si+i][sj+j]=arr[si+i][sj+j-half]    # arr에서 가져오는 거니까 뺴야지

        for i in range(half,l):
            for j in range(half):  # 4 -> 3
                new_arr[si + i][sj + j] = arr[si + i][sj + j+half]
            for j in range(half,l): # 2 -> 4
                new_arr[si + i][sj + j] = arr[si + i-half][sj+j]
'''

N,Q=map(int,input().split())
N=2**N                                  # 한 변의 길이
arr=[list(map(int,input().split())) for _ in range(N)]
rt=list(map(int,input().split()))

# ==================================
for l in rt:
    if l != 0:
        l=2**l
        half=l//2
        new_arr=[[0]*N for _ in range(N)]
        # 1 2 -> # 3 1
        # 3 4    # 4 2  로 돌리고 싶은 거
        for si in range(0,N,l):
            for sj in range(0,N,l):
                for i in range(half):
                    for j in range(half):   # 3 -> 1
                        new_arr[si+i][sj+j]=arr[si+i+half][sj+j]
                    for j in range(half,l): # 1 -> 2
                        new_arr[si+i][sj+j]=arr[si+i][sj+j-half]    # arr에서 가져오는 거니까 뺴야지

                for i in range(half,l):
                    for j in range(half):  # 4 -> 3
                        new_arr[si + i][sj + j] = arr[si + i][sj + j+half]
                    for j in range(half,l): # 2 -> 4
                        new_arr[si + i][sj + j] = arr[si + i-half][sj+j]

        arr = new_arr


    temp=[row[:] for row in arr]
    for i in range(N):
        for j in range(N):
            if temp[i][j] > 0:
                cnt = 0
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and temp[ni][nj] > 0:
                        cnt += 1
                if cnt < 3:
                    arr[i][j] -= 1


# ===========================
from collections import deque

def bfs(i,j):
    q=deque([(i,j)])
    v[i][j]=1
    cnt=1

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]>0 and v[ni][nj]==0:
                v[ni][nj]=1
                q.append((ni,nj))
                cnt+=1

    return cnt

v=[[0]*N for _ in range(N)]
ans=1
for i in range(N):
    for j in range(N):
        if arr[i][j]>0 and v[i][j]==0:
            ans=max(ans,bfs(i,j))

print(sum(map(sum,arr)))
if ans==1:
    print(0)
else:
    print(ans)

'''

B20058 마법사 상어와 파이어스톰 / 2025-03-05 / 체감 난이도 : 골드 3
소요 시간 : 3시간 / 시도 : 2회 (틀렸습니다 -> 성공)

[0] 총평
- 배열 돌리기에서 삽질을 많이 했고 당황하니 이상한 짓을 너~무 많이 함
-> 침착하게 .. 천천히.. 조급해지면 멘탈 나가고 이상한 짓 많이 하고 발견도 못함 그러니 의식적으로 심호흡을 하던지 화장실을 다녀오던지

- 4중 for문을 쓰면서 스스로 아.. 역시 내 아이디어는 비효율적이야 이러면서 자신감이 떨어짐 근데 준영프로님 코드보니까 맞네 ;;;
자신감을 좀 갖고 하기 !!! + 시간 복잡도 계산을 해보던가

[1] 타임라인
1. 문제 이해 및 구상 (10분) -> 일단 회전하는게 관건이구나 .. 생각하고
2. 회전 구현 (1시간 30분)
- 처음 시도는 4중 포문을 돌리면서 2**L 크기 만큼 배열 슬라이싱 + 좌표 기록 + 배열을 전치행렬 써서 돌리고 기록해둔 좌표에 회전한 배열의 값을 쓰기
-> 1시간 붙잡고 했는데 안 되어서 슬라이싱 말고 좌표로 시도
( 안 되던 이유는 슬라이싱 할 때 [row[i:~] for row in arr[i~]] 이렇게 둘다 x좌표로 했음 ;;)

- new[i][j]=arr[2**num-1-j][i] 이런 식으로 90도 회전했을 때 어디로 돌아가는지 규칙성 찾아서 하고 싶었는데 이것도 안됨 ( ** 다시 해보기 )
30분째 붙잡고 하다가 .. 다시 처음 방법으로 돌아와서 해결

3. 나머지 구현 (30분)
시간이 없으니  마음이 급해서 이상한 실수 와장창 2**N을 N으로 써놓고 오잉? 테케 다른 거 돌려놓고 답 이상해서 엥? 하고 있었음
침착하자 !!!

[2] 배운점 및 실수한 점
- 배열 돌리기 하는 방법 ( 준영프로님 코드 참조 )
 for n in range(N // l):
        for m in range(N // l):  # 전체 배열을 (2^l)*(2^l)로 나누면 (2^(N-l))*(2^(N-l)) 개가 생김
            for i in range(l):  # i행 j열을 돌릴거다,
                for j in range(l):  # 그냥 크기 (2**l) * (2**l)을 돌리는 거면 (i,j)자리에 오는건 이전 배열의 (2**l-1-j,i) 요소이다.
                    tmp[l * n + i][l * m + j] = arr[l * n + l - 1 - j][l * m + i]

'''

from collections import deque

# 회전하는 함수
def rotate(temp):
    temp=list(map(list,zip(*temp)))
    new=[]
    for row in temp:
        for num in row[::-1]:
            new.append(num)
    return new

# 얼음이 0 이거나 범위 밖인 개수를 세는 함수 -> 2 이상이면 줄여
def bfs(i,j):
    cnt=0
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=i+di,j+dj
        if ni<0 or 2**N<=ni or nj<0 or 2**N<=nj or arr[ni][nj]==0:
            cnt+=1
    return cnt

def check(i,j):
    # cnt로 개수 세준다
    global cnt
    v = [[0] * (2 ** N) for _ in range(2 ** N)]
    cnt = 1
    v[i][j]=cnt

    while q:
        ci,cj=q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<2**N and 0<=nj<2**N and arr[ni][nj]!=0 and v[ni][nj]==0:
                q.append((ni,nj))
                cnt += 1
                v[ni][nj] = cnt
    return cnt

N,Q=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(2**N)]
L=list(map(int,input().split()))

for num in L:
    final = [[0] * (2 ** N) for _ in range(2 ** N)]
    I=0
    J=0

    # loc에다가 좌표를 담는 거고
    for I in range(0,2**N,2**num):
        loc = []
        for J in range(0,2**N,2**num):
            loc = []
            for i in range(I,I+2**num):
                for j in range(J,J+2**num):
                    loc.append((i,j))

            # temp에 슬라이싱
            temp=[row[loc[0][1]:loc[-1][1]+1] for row in arr[loc[0][0]:loc[-1][0]+1]]
            new=rotate(temp)

            # 슬라이싱해서 회전한 걸 final에 다시 쓰기
            for i in range(len(loc)):
                x,y=loc[i]
                arr[x][y]=new[i]

    change=[]

    for i in range(2**N):
        for j in range(2**N):
            # 2이상이여서 줄여야 하는 거 change에 append
            if arr[i][j] !=0 and bfs(i,j) >= 2 :
                change.append((i,j))
    # 줄여
    for R,C in change:
        arr[R][C]-=1


sm=0
mx=0

for i in range(2**N):
    for j in range(2**N):
        sm+=arr[i][j]
        # 0이 아닐 때만 bfs 돌려서 갱신
        if arr[i][j]!=0:
            q = deque()
            q.append((i, j))
            ans=check(i, j)
            mx=max(mx,ans)

print(sm)
print(mx)
