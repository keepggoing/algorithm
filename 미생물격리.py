T=int(input())                      # 테케 개수
for tc in range(1,T+1):
    # 한 변에 있는 셀의 개수, 격리 시간, 미생물 군집
    N,M,K=map(int,input().split())
    arr=[[0]*N for _ in range(N)]

    for j in range(N):
        arr[0][j]=1
        arr[-1][j]=1

    for i in range(1,N-1):
        arr[i][0]=1
        arr[i][-1]=1
    # ==================================================
    dic={1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}
    change_dic={1:2,2:1,3:4,4:3}
    p={}

    for _ in range(K):
        r,c,n,d=map(int,input().split())
        p[(r,c)]=[(n,d)]

    for _ in range(M):             # M번의 턴 동안
        new_p={}
        for key,value in p.items():
            r,c=key[0],key[1]
            n,d=value[0][0],value[0][1]
            di,dj=dic[d]
            ni,nj=r+di,c+dj

            if arr[ni][nj] == 1:
                if (ni, nj) not in new_p:
                    new_p[(ni, nj)] = [(n//2, change_dic[d])]
                else:
                    new_p[(ni, nj)].append((n//2, change_dic[d]))

            else:
                if (ni, nj) not in new_p:
                    new_p[(ni, nj)] = [(n,d)]
                else:
                    new_p[(ni, nj)].append((n,d))

        # 다 돌고 나서 new_p에 두개 이상이면
        for key, value in new_p.items():
            if len(value)>=2:
                value.sort(key=lambda x: -x[0])
                sm=0
                for n,d in value:
                    sm+=n
                mx=value[0][1]
                new_p[key]=[(sm,mx)]
        p=new_p
    ans=0
    for key,value in p.items():
        ans+=value[0][0]
    print(f'#{tc} {ans}')           # M시간 후 남아있는 미생물 수의 총합을 구하기