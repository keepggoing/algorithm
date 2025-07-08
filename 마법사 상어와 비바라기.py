''' 2차 풀이
[0] 타임라인
구상 (15분)
구현 (10분)
디버깅 (10분)

[1] 실수한 점
1. 방향 딕셔너리 잘못 쓰는 실수 드디어 나옴 -> 체크리스트 추가하기
2. 특수 영양제 투입한 거는 제외해야하는데 안함 ( 문제 조건 누락 )
3. 틀린 건 아니지만 아래처럼 하면 반복문에서 계속 set으로 바꿈 위에서 한번만 바꿔주면 됨

    new_nut=[]
    for i in range(N):
        for j in range(N):
            if arr[i][j]>=2 and (i,j) not in set(nut):
                arr[i][j]-=2
                new_nut.append((i,j))

    nut=new_nut

[2] 배울점
1. 이 풀이 이후로 간격 맞춰 출력할 때 아래 코드 외워서 사용할 거임
for row in arr:
    print(''.join(f'{x:4}' for x in row))

'''

# 격자의 크기, 총 년 수
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
dic={1:(0,1),2:(-1,1),3:(-1,0),4:(-1,-1),5:(0,-1),6:(1,-1),7:(1,0),8:(1,1)}

nut=[(N-2,0),(N-2,1),(N-1,0),(N-1,1)]

for _ in range(M):
    # 이동 방향, 이동 칸수
    d,p=map(int,input().split())
    di,dj=dic[d]

    for i in range(len(nut)):
        si,sj = nut[i]
        ni,nj=(si+di*p)%N,(sj+dj*p)%N
        nut[i]=(ni,nj)

    for si,sj in nut:
        arr[si][sj]+=1

    for si,sj in nut:
        cnt=0
        for di,dj in (dic[2],dic[4],dic[6],dic[8]):
            ni,nj=si+di,sj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] >=1:
                cnt+=1
        arr[si][sj]+=cnt

    nut=set(nut)
    new_nut=[]
    for i in range(N):
        for j in range(N):
            if arr[i][j]>=2 and (i,j) not in nut:
                arr[i][j]-=2
                new_nut.append((i,j))

    nut=new_nut

    #for row in arr:
    #    print(''.join(f'{x:4}' for x in row))

print(sum(map(sum,arr)))


'''
마법사 상어와 비바라기 (3/) / 2025-03-04 / 체감 난이도 : 골드 4
소요 시간 : 2시간 / 시도 : 4회 / 실행 시간 : 188ms / 메모리 : 112636KB

[배운점 !!!!]
1) 리스트에서 in 또는 not in 연산은 O(k) (k는 리스트 크기) 시간이 걸린다
그래서 조회할 때는 set으로 하던가 visited 관리를 해주던가

2) 튜플은 특정 원소만을 수정할 수 없으니까 어떻게 고쳐야하는지 순간 헷갈렸는데 걍 아래처럼 하면 됨
v[i][0], v[i][1] = ni, nj -> v[i] = (ni,nj)

[타임라인]
1. 문제 이해 & 구상 (30분)
2. 구현 (20분)
3. 1차 제출 후 시간초과
4. 시간초과 계산 및 리팩토링 시도.. (1시간)
- in/not in 때문일 거라고 생각을 못했음..
로직에 문제 없다는 걸 느꼈으면 다른 부분을 봐야지 !!

[디버깅 내역]
- 시간초과를 위해 1,2,3 단계를 하나의 for문에서 합치려고 했는데 그러니 오픈 테케 답이 안 맞음
- 애초에 시간초과 계산도 잘못했음
not in 때문에 3중 for문이 되는 거였는데 !!!

[구상]
[1] 모든 구름이 (4개) d 방향으로 s칸 이동한다
[2] 구름이 이동한 위치의 바구니에 물을 +1 한다
[3] 구름이 모두 사라진다 (필요없음)
[4] [2]에서 증가한 칸에 물복사버그 마법을 사용한다
-> 단, 이때는 경계 넘어가면 짤라야함

[5] 바구니에 저장된 물의 양이 2 이상인 곳에 구름이 생기고 물의 양이 2 준다
이 때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다
-> 단, 나머지 칸이여야 한다 ! !!!!

[구현]

[마지막 체크 포인트]

[후기]
테케가 틀리거나 뭔가 잘못된 게 있을 때 왜이렇게 당황하고 멘탈이 흔들릴까? 마음 단단히 먹기 ! 틀려도 고칠 수 있닥 !
시간초과가 뜨니 또 풀이 확 죽었는데 set으로 이렇게 간단하게 해결할 수 있는 건 줄 몰랐다 ( 그냥 set이 내 머릿속에 없었음 )
스스로에 대한 적당한 자신감과 확신을 가진채 차근 차근 문제를 해결해나가보자 !

'''

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
v=[(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
dr={1:(0,-1), 2:(-1,-1), 3:(-1,0), 4:(-1,1), 5:(0,1), 6: (1,1), 7:(1,0), 8:(1,-1)}
# M개의 이동
for _ in range(M):
    # [1] 1단계
    d,s=map(int,input().split())
    for i in range(len(v)):
        si, sj = v[i][0], v[i][1]
        # d방향 s칸을 적용해서 q에 넣는다
        ni, nj = si + dr[d][0] * s, sj + dr[d][1] * s

        if ni < 0:
            if -ni%N==0:
                ni=0
            else:
                ni = N - (-ni % N)
        elif ni >= N:
            ni = ni % N

        if nj < 0:
            if -nj % N == 0:
                nj = 0
            else:
                nj = N - (-nj % N)

        elif nj >= N:
            nj = nj % N

        v[i] = (ni, nj)
        arr[ni][nj] = arr[ni][nj] + 1

    # [3] 3단계
    for m, n in v:
        cnt = 0
        for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            ni, nj = m + di, n + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                cnt += 1

        arr[m][n] += cnt

    # [4] 4단계
    # 복사가 오래 걸려..?
    temp = set(v)
    v = []

    for i in range(N):
        for j in range(N):
            if (i, j) not in temp and arr[i][j] >= 2:
                v.append([i, j])
                arr[i][j] -= 2

result=0
for row in arr:
    result+=sum(row)
print(result)