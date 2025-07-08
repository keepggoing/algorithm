T=int(input())
def make(si,sj,l1,l2):
    lst = [arr[si][sj]]

    di,dj=1,1
    for _ in range(l1):
        si,sj=si+di,sj+dj
        if si<0 or si>=N or sj<0 or sj>=N:
            return -1
        else:
            lst.append(arr[si][sj])

    di,dj=1,-1
    for _ in range(l2):
        si,sj=si+di,sj+dj
        if si<0 or si>=N or sj<0 or sj>=N:
            return -1
        else:
            lst.append(arr[si][sj])

    di,dj=-1,-1
    for _ in range(l1):
        si,sj=si+di,sj+dj
        if si<0 or si>=N or sj<0 or sj>=N:
            return -1
        else:
            lst.append(arr[si][sj])

    di,dj=-1,1
    for _ in range(l2):
        si,sj=si+di,sj+dj
        if si<0 or si>=N or sj<0 or sj>=N:
            return -1
        else:
            lst.append(arr[si][sj])

    if lst[0]==lst[-1]:
        lst.pop()
        if len(lst) == len(set(lst)):
            return len(lst)
        else:
            return -1
    return -1

for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    mx=-1
    # 시작점
    for si in range(0,N-2):
        for sj in range(1,N-1):
            for l1 in range(1,N-1):
                for l2 in range(1,N-1):
                    mx=max(mx,make(si,sj,l1,l2))

    print(f'#{tc} {mx}')