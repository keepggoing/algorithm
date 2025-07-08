T=int(input())
for tc in range(1,T+1):
    # N행 M열, K 개의 말, ei,ej는 목적지
    # 직사각형 200 x 200 , 말은 50개 이하
    N,M,K,ei,ej=map(int,input.split())
    # 목적지는 하나씩 줄인다
    ei,ej=ei-1,ej-1
    # 말의 위치
    loc=[list(map(lambda x: int(x)-1, input().split()))]
    # 벽이 W, 빈칸이 .
    arr=[list(input()) for _ in range(N)]

    wall=[]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                wall.append((i,j))

    # 한 번까지 부수고 가기






    # 출력
    # 기존 게임의 점수 D, 모든 벽의 가치 총합