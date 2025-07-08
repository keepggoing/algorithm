'''
B17143 낚시왕 / 2025-03-20 / 체감 난이도 : 골드 2
소요 시간 : 2시간 / 시도 : 1회

[0] 총평
- 문제를 풀다보니 3차원 배열을 활용할 일이 많음..
리스트로 몇번 감쌌는지 헷갈리는 경우가 많으니 이럴 땐 디버거보다 프린트로 디버깅 해보는 것이 좋다 !

[1] 타임라인
1. 문제 이해 및 구상 (30분)

2. 구현 (30분)

3. 디버깅 (1시간)
-> "s, d, z = arr[nnn][mmm][0][0], arr[nnn][mmm][0][1], arr[nnn][mmm][0][2]"
이 부분에서 자꾸 int object is not subscriptable 이라는 오류가 떠서.. 고생했다
디버거로 보고는 발견을 하지 못해서 다시 짜다가 print로 찍어서 발견


[2] 배운점 및 실수한 점
벽을 찍고 방향을 바꿔서 다시 갈 때 주기 있음 s = s % (2 * (l - 1)) 이거..
이거 다시 해보기 !!
'''
R,C,M=map(int,input().split())
arr=[[[] for _ in range(C)] for _ in range(R)]
ans=0
man=0

di=[-1,1,0,0]
dj=[0,0,1,-1]

change={0:1,1:0,2:3,3:2}

for _ in range(M):
    r,c,s,d,z=map(int,input().split())
    r,c,d=r-1,c-1,d-1
    arr[r][c].append((s,d,z))

if M==0:
    print(0)
else:
    for man in range(0,C):
        for i in range (0,R):
            if len(arr[i][man]) != 0:
                ans+=arr[i][man][0][2]
                # 이렇게 해도 됨 왜냐하면 어떻게든 잡아먹고 하나가 되기 때문에
                arr[i][man]=[]
                break

        # 잡아먹고 나서 움직여야지
        need=[]
        for nn in range(R):
            for mm in range(C):
                if len(arr[nn][mm]) != 0:
                    need.append((nn,mm))

        for nnn,mmm in need:
            s, d, z = arr[nnn][mmm][0][0], arr[nnn][mmm][0][1], arr[nnn][mmm][0][2]
            tmp = 0
            # 움직이는 도중에는 한 칸에 두개일 수 있기 때문에
            # 함부로 0으로 바꾸면 안 된다
            arr[nnn][mmm].pop(0)
            x,y = nnn,mmm
            while tmp < s:
                x, y = x + di[d], y + dj[d]
                if x < 0 or x >= R or y < 0 or y >= C:
                    x, y = x - di[d], y - dj[d]
                    d = change[d]
                    x, y = x + di[d], y + dj[d]
                tmp += 1
            arr[x][y].append((s, d, z))

        # 만약 두개가 있다면 더 작은 거를 잡아먹는다 !
        for i in range(R):
            for j in range(C):
                if len(arr[i][j])>=2:
                    arr[i][j].sort(key=lambda x: x[2])
                    arr[i][j]=[arr[i][j][-1]]

    print(ans)