T=int(input())

for tc in range(1,T+1):
    # 벌통의 크기, 선택할 수 있는 벌통 개수, 꿀을 채취할 수 있는 최대 양
    N,M,C=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    tp=[]
    for r in range(N):
        row=arr[r]
        for i in range(0,N-M+1):
            temp=row[i:i+M]
            temp.sort(reverse=True)
            print(temp)
            sm=0
            ans=0
            for j in range(M):
                if sm+temp[j]<=C:
                    ans+=(temp[j])**2
                else:
                    break
            tp.append((ans,i,j))

    tp.sort(key=lambda x: -x[0])
    print(tp)
