T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]

    # 중간
    mid=N//2
    #print(arr)

    #시작점
    si,sj,sm=0,mid,0
    sm+=arr[si][sj]

    #각 행에서 구해야 하는 개수
    size=1

    while si<N//2 and sj>0:
        si,sj=si+1,sj-1
        size+=2
        sm+=sum(arr[si][sj:sj+size])

    while si<N and sj<mid:
        si,sj=si+1,sj+1
        size-=2
        sm+=sum(arr[si][sj:sj+size])
    print(f'#{tc} {sm}')