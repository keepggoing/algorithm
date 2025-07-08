def play(si,sj,d):
    ans=0       # 점수
    ci,cj=si,sj

    while True:
        di,dj=dic[d]
        ni,nj=si+di,sj+dj
        if ni<0 or ni>=N or nj<0 or nj>=N:  # 범위 밖이면 방향만 바꿔
            ans+=1
            si,sj=ni,nj                     # 범위 밖이지만 일단 보내?
            d=(d+2)%4                       # si,sj 안 바뀌고 그자리에서 한 번 더 해봐

        else:                               # 범위 내 이고
            if arr[ni][nj]==0:              # 빈 곳이면
                si,sj=ni,nj                 # 현재 위치 바꿔

            elif arr[ni][nj]==-1:           # 블랙홀 만나면 종료
                return ans

            elif arr[ni][nj]==1:
                ans+=1                      # 일단 점수 하나 올리고
                si,sj=ni,nj
                if d in ch_1:
                    d=ch_1[d]
                else:
                    d=(d+2)%4

            elif arr[ni][nj]==2:
                ans+=1                      # 일단 점수 하나 올리고
                si,sj=ni,nj
                if d in ch_2:
                    d=ch_2[d]
                else:
                    d=(d+2)%4

            elif arr[ni][nj]==3:
                ans+=1                      # 일단 점수 하나 올리고
                si,sj=ni,nj
                if d in ch_3:
                    d=ch_3[d]
                else:
                    d=(d+2)%4

            elif arr[ni][nj]==4:
                ans+=1                      # 일단 점수 하나 올리고
                si,sj=ni,nj
                if d in ch_4:
                    d=ch_4[d]
                else:
                    d=(d+2)%4

            elif arr[ni][nj]==5:
                si,sj=ni,nj
                ans+=1
                d=(d+2)%4

            elif 6<=arr[ni][nj]<=10:
                for x,y in warm[arr[ni][nj]]:
                    if (x,y) != (ni,nj):
                        si,sj=x,y

        if (si,sj)==(ci,cj):
            return ans

T=int(input())              # 테케 개수
dic={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}     # 상, 우, 하, 좌 순서
ch_1={2:1,3:0}                              # 1일 땐
ch_2={3:2,0:1}
ch_3={1:2,0:3}
ch_4={1:0,2:3}

for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]      # 게임판
    mx=0
    warm = {}
    for i in range(N):
        for j in range(N):
            if 6<=arr[i][j]<=10:
                if arr[i][j] not in warm:
                    warm[arr[i][j]]=[(i,j)]
                else:
                    warm[arr[i][j]].append((i,j))
    # 0인 곳은 네방향을 다 해본다
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for d in range(0,4):
                    ans=play(i,j,d)
                    mx=max(ans,mx)
    print(f'#{tc} {mx}')