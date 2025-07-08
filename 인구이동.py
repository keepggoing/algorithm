'''
### 코드 리뷰 ###

B16234 인구이동 / 2025-03-05 / 체감 난이도 : 골드 5
소요 시간 : 1시간 5분 / 시도 : 2회 (틀렸습니다 -> 성공)

[0] 총평
- 그냥 bfs 문제네? 라고 생각하고 sudo code 작성 안 하고 덤빔
앞으로 한 번 더 걍 덤비면 진짜... 에바다

[1] 타임라인
1. 문제 이해 및 구상 (8분)
2. 구현 (20분)
-> 틀렸습니다
한 번 더 차분히 읽고 제출하는 거 왜 안 하셨는지 ?
3. 디버깅 (30분)
-> 예제 단계별로 돌리면서 한 국경인게 어떻게 표시되는지 찍어봄

[2] 배운점 및 실수한 점
- 이미 다른 나라랑 연결 되어있었는데 또 다른 나라랑 연결되면 그 전체를 하나로 봐야하는데 그 처리를 안 해줌
-> 특히 이번 문제처럼 잘못 돌아가도 답은 잘 나올 가능성이 있는 문제들은 꼭꼭 과정을 찍어봐야 함 !!!

'''
# visited 배열 안에 같은게 있는지 없는지 확인하는 함수
# 같은게 하나라도 있으면 더 해야해
def check(v):
    temp=[]
    for row in v:
        for num in row:
            temp.append(num)
    # 같은게 없다 -> 더 해야한다
    if len(temp) != len(set(temp)):
        return 1
    else:
        return 0

def bfs(i,j):
    global num

    # 만약에 아직 방문을 안 한 거로 되어 있으면
    # 새로운 수 넣어준다
    if v[i][j] == 0:
        v[i][j]=num
        num+=1

    # 아니면 계속 연결해준다
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=i+di,j+dj
        # 이미 연결됐으면 안 되니까
        if 0<=ni<N and 0<=nj<N:
            sub=abs(arr[ni][nj]-arr[i][j])
            if L<=sub and sub<=R:
                if v[ni][nj]==0:
                    v[ni][nj]=v[i][j]
                elif v[ni][nj]!=v[i][j]:
                    pivot=v[ni][nj]
                    v[ni][nj]=v[i][j]
                    for r in range(N):
                        for c in range(N):
                            if v[r][c]==pivot:
                                v[r][c]=v[i][j]
N,L,R=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

day=0

while True:
    num = 1
    # visited 배열에 같은 국경선인 걸 표시할 거야
    # 다시 초기화함으로써 연합 해체 및 국경선 닫음
    v = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            bfs(i,j)
    dic={}
    for i in range(N):
        for j in range(N):
            if v[i][j] not in dic:
                dic[v[i][j]]=[(i,j)]
            else:
                dic[v[i][j]].append((i,j))

    for key in dic:
        l=len(dic[key])
        sm=0
        for x,y in dic[key]:
            sm+=arr[x][y]
        sm=sm//l
        for x,y in dic[key]:
            arr[x][y]=sm

    if not check(v):
        print(day)
        break

    # 하루 추가
    day+=1
