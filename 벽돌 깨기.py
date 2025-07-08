T=int(input())

def breakk(hit, arr):
    while hit:
        hi, hj, l = hit.pop()
        arr[hi][hj]=0
        if l >= 2:
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                for mul in range(1, l):
                    ni, nj = hi + di * mul, hj + dj * mul
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0:
                        if arr[ni][nj] >= 2:
                            hit.append((ni, nj, arr[ni][nj]))
                        arr[ni][nj]=0
    return arr

def downn(arr):
    new_arr = [[0] * M for _ in range(N)]

    for j in range(0, M):
        I = N - 1
        for i in range(N - 1, -1, -1):
            if arr[i][j] != 0:
                new_arr[I][j] = arr[i][j]
                I -= 1
    arr = new_arr

    return arr

def btk(cnt,arr):
    global ans

    if cnt == K:
        sm=0
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    sm+=1

        ans=min(ans,sm)
        return

    for j in range(M):
        hit = []
        for i in range(0,N):
            if arr[i][j] != 0:
                hit.append((i,j,arr[i][j]))
                break
        else:
            continue
        temp = [row[:] for row in arr]
        temp = breakk(hit, temp)
        temp = downn(temp)
        btk(cnt + 1, temp)
    else:
        btk(cnt+1,arr)


for tc in range(1,T+1):
    K,M,N=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    ans=N*M
    btk(0,arr)
    print(f'#{tc} {ans}')
