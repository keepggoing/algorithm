''' 2차 풀이
[0] 타임라인
구상 (30분)
구현 (40분)
디버깅 (10분)

[1] 실수한점
1. flag를 True로 두고 하고 있었음
2. "다른 격자에 이동한 먼지의 양을 모두 합한 것 " -> 격자 밖에 나간 것도 포함인데 아니라고 생각했음

[2] 배운점
1. 애매한 건 오픈테케로 검증, 확인하고 넘어가야함
'''

# 왼쪽 - 아래 - 오른쪽 - 위
dic={0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}
per=[[[(-1,0),(1,0)],[(-2,0),(2,0)],[(-1,1),(1,1)],[(-1,-1),(1,-1)],[(0,-2)],[(0,-1)]],
     [[(0,-1),(0,1)],[(0,-2),(0,2)],[(-1,-1),(-1,1)],[(1,-1),(1,1)],[(2,0)],[(1,0)]],
     [[(-1,0),(1,0)],[(-2,0),(2,0)],[(-1,-1),(1,-1)],[(-1,1),(1,1)],[(0,2)],[(0,1)]] ,
     [[(0,-1),(0,1)],[(0,-2),(0,2)],[(1,1),(1,-1)],[(-1,-1),(-1,1)],[(-2,0)],[(-1,0)]]]
percent=[7,2,1,10,5]

# ================================
ans=0
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
si,sj=N//2,N//2
d=0
cnt=1                   # 반복횟수
flag=False
while True:
    for _ in range(2):
        for _ in range(cnt):
            di, dj = dic[d]
            ni,nj=si+di,sj+dj
            pivot=arr[ni][nj]
            arr[ni][nj]=0
            sm=0

            for i in range(5):
                for ddi,ddj in per[d][i]:
                    nni,nnj=ni+ddi,nj+ddj
                    if nni<0 or nni>=N or nnj<0 or nnj>=N:
                        ans+= pivot * percent[i] // 100
                        sm+= pivot * percent[i] // 100
                    else:
                        arr[nni][nnj]+=pivot*percent[i] // 100
                        sm+=pivot*percent[i] // 100
            nni,nnj=ni+per[d][5][0][0],nj+per[d][5][0][1]
            if nni < 0 or nni >= N or nnj < 0 or nnj >= N:
                ans += pivot-sm
            else:
                arr[nni][nnj] += pivot - sm

            si,sj=ni,nj
            if (si,sj) == (0,0):
                flag=True
                break

        d=(d+1)%4
        if flag:
            break
    cnt+=1
    if flag:
        break
print(ans)


'''
B20057 마법사 상어와 토네이도 / 2025-03-11 / 체감 난이도 : 골드 3
소요 시간 : 1시간 (재시도) / 시도 : 1회

[0] 총평
- 방향마다 달라지는 모래가 날리는 양을 어떻게 관리해야할지 고민함
-> 지금껏 보기만 했지 내가 직접 룩업테이블을 만들어본 적이 없는 것 같다
기억하자 정해진 건 룩업테이블로 기록해두면 쉽게 풀린다 !

[1] 타임라인
1. 문제 이해 및 구상 , 달팽이 구현 (1시간)
-> 달팽이 해보다가 1시간이 슝 갔음 하지만 그마저도 잘못함

2. 구현 (30분)
-> 이것도 방향마다 분기로 나눠서 짜보다가 시간이 날라갔다
짜다가 철회하는 거만큼 시간이 아까운게 없다.. 될 거 같은 걸 해라

3. 디버깅 (30분)
-> 나눠서 확인해봤음 됐는데 긴 코드에서 달팽이 확인하려니 복잡하다보니 꼬임

[2] 배운점 및 실수한 점
- 실수 계산은 항상 지양하자
- 아이디어 안 날때는 룩업테이블이 있잖아 !!!!
정해진 건 만들어 놓으면 된다
- 작은 단위로 나눠서 달팽이 먼저 돌아가는지 확인하고 다음 꺼 차근차근 했으면 됐다
유닛테스트 꼭 하기 **

'''
N = int(input())
si, sj = N // 2, N // 2

arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
dr = 0

amount=[ 2,10, 7, 1, 5,10, 7, 1, 2, 0]
gi=[[-2,-1,-1,-1, 0, 1, 1, 1, 2, 0],
    [ 0, 1, 0,-1, 2, 1, 0,-1, 0, 1],
    [ 2, 1, 1, 1, 0,-1,-1,-1,-2, 0],
    [ 0,-1, 0, 1,-2,-1, 0, 1, 0,-1]]
gj=[[ 0,-1, 0, 1,-2,-1, 0, 1, 0,-1],
    [-2,-1,-1,-1, 0, 1, 1, 1, 2, 0],
    [ 0, 1, 0,-1, 2, 1, 0,-1, 0, 1],
    [ 2, 1, 1, 1, 0,-1,-1,-1,-2, 0]]

out = 0
dist = 1
flag = False
result=0

while True:
    for _ in range(2):
        for mul in range(1, dist + 1):
            if (si, sj) == (0, 0):
                flag = True
                break
            ei, ej = si + di[dr], sj + dj[dr]
            if arr[ei][ej] > 0:
                pivot = arr[ei][ej]
                sm = 0

                for k in range(10):
                    ti = ei + gi[dr][k]
                    tj = ej + gj[dr][k]
                    a = pivot*amount[k]//100

                    if k==9:
                        a=pivot-sm
                    if 0 <= ti < N and 0 <= tj < N:
                        arr[ti][tj] += a

                    else:
                        result+=a
                    sm += a

                arr[ei][ej] = 0

            # 마지막에 그 자리로 시작 위치 바꿔
            si, sj = ei, ej
        # mul 만큼 돌고 나면 방향 바꾸는 거고
        dr = (dr + 1) % 4
        if flag:
            break
    dist += 1
    if flag:
        break

print(result)