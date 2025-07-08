T=int(input())

def find_block(j,tidx,didx):
    for idx in range(tidx + 1, N):
        if arr[idx][j] == 0:
            didx = idx - 1
            return tidx, didx
    return tidx, N - 1

# 열을 하나씩 본다
def solve():
    for j in range(N):
        # 가장 위에 없다면 넘어감
        if arr[0][j] == 0: continue
        # 시작 0번 인덱스, 끝 0번 인덱스, power은 1
        now=[0,0,1]

        tidx=1
        didx=1

        while True:
            if tidx>=N: break
            # tidx 1부터 봐서 만약 블록이 있다면
            if arr[tidx][j] == 1:
                tidx,didx=find_block(j,tidx,didx)

                # 지금 만난 장애물은 tidx~didx
                opower = didx - tidx + 1
                # 더 클 때만 합쳐지고 또 아래로 내려감
                if now[2] > opower:
                    # 힘은 더해지고
                    now[2] += opower
                    now[1] = didx
                    tidx=didx+1
                # 더 안 크다면 멈춤
                else: break
            else:
                now[0]+=1
                now[1]+=1
                now[2]*=1.9
                tidx+=1

        if now[0] != 0:
            start,end=now[0],now[1]
            for i in range(0,start):
                arr[i][j]=0
            for i in range(start,end+1):
                arr[i][j]=1

for tc in range(1,T+1):
    # 정사각형 (<= 500)
    N=int(input())
    # 블록이 있으면 1, 없으면 0
    arr=[list(map(int,input().split())) for _ in range(N)]

    solve()
    arr=list(map(list,zip(*arr[::-1])))
    solve()
    arr=list(map(list,zip(*arr)))[::-1]

    # 맨 아래 행에 자리한
    # 블록의 수와 맨 오른쪽 역에 자리한 블록의 수를 차례로 나열하라.
    ans1=sum(arr[-1])
    ans2=0
    for i in range(N):
        ans2+=arr[i][-1]
    print(f'#{tc} {ans1} {ans2}')
