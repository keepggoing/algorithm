# 상근이네 집에서 출발 ( 맥주 한 박스 들고 출발 (20병))
# 50m에 한병씩 -> 한 박스당 1000m 갈 수 있음
# 편의점 들린 이후로는 항상 20병이 채워진다
# 편의점 들려서 어쨋든 페스티벌에 도착할 수 있는지 구하기
T=int(input())
for tc in range(T):
    N=int(input())
    info=[]
    for i in range(N+2):
        x,y=map(int,input().split())
        info.append((x,y))

    # ===== 전처리 끝
    arr=[[0]*(N+2) for _ in range(N+2)]

    for i in range(N+2):
        for j in range(i+1,N+2):
            if abs(info[i][0]-info[j][0])+abs(info[i][1]-info[j][1])<= 1000:
                arr[i][j]=1
                arr[j][i]=1

    for k in range(N+2):
        for i in range(N+2):
            for j in range(N+2):
                if arr[i][j]==1 or i==j or j==k or i==k:
                    continue
                # i-k 1 k-j 1 i-j 1
                # 비트연산자 and - 1 1 일 때만 1
                arr[i][j] = arr[i][k]&arr[k][j]

                if arr[i][k]==1 and arr[k][j]==1:
                    arr[i][j]=1

    if arr[0][N+1]==1:
        print("happy")
    else:
        print("sad")






