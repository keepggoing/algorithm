'''
B16235 나무 재테크 / 2025-03- / 체감 난이도 : 골드 3
소요 시간 : 2시간 (실패) - 1시간 (재풀이) / 시도 : 2회

[0] 총평
- 시간 초과가 났다 그냥 짜니까
- 모든 단계를 하나씩 해내가는 것도 좋지만 합칠 수 있는 건 합치는게 좋다

[1] 타임라인
1. 문제 이해 및 구상

2. 구현

3. 디버깅

[2] 배운점 및 실수한 점

'''




from collections import deque

N,M,K=map(int,input().split())
# 채워야할 양
fill=[list(map(int,input().split())) for _ in range(N)]
# 현재 양분
arr=[[5]*N for _ in range(N)]
# 트리 딕셔너리
tree={}

for _ in range(M):
    x,y,age=map(int,input().split())
    x,y=x-1,y-1
    if (x,y) not in tree:
        # 만들어주고
        tree[(x,y)]=deque()
        # 정렬 필요 없이 걍 넣어줘됨 처음에 같은 위치 안 나온다 했으니까
        # 그리고 나서 앞에 넣어주기
    # 항상 append
    tree[(x,y)].append(age)

# K번 반복한다
for _ in range(K):
    die = {}
    new_tree={}
    # 봄
    for x,y in (tree.keys()):
        survived=deque()
        dead=0
        for age in tree[(x,y)]:
            if arr[x][y]>=age:
                arr[x][y]-=age
                survived.append(age+1)
            else:
                dead+=age//2
        tree[(x,y)]=survived
        if dead>0:
            die[(x, y)]=dead


    # 여름
    for (x,y),amount in die.items():
        arr[x][y]+=amount

    # 가을
    for (x, y) in tree:
        for age in tree[(x, y)]:
            if age%5==0:
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)):
                    ni,nj=x+di,y+dj
                    if 0<=ni<N and 0<=nj<N:
                        if (ni,nj) not in new_tree:
                            new_tree[(ni, nj)] = deque()
                        new_tree[(ni, nj)].append(1)

    for (x,y) in new_tree:
        if (x,y) in tree:
            tree[(x, y)].extendleft(new_tree[(x, y)])
        else:
            tree[(x, y)] = new_tree[(x, y)]
    # 겨울
    for i in range(N):
        for j in range(N):
            arr[i][j]+=fill[i][j]


ans=0
for key in tree:
    ans+=len(tree[key])
print(ans)


''' 시간초과난 코드
N,M,K=map(int,input().split())
# 채워야할 양
fill=[list(map(int,input().split())) for _ in range(N)]
# 현재 양분
arr=[[5]*N for _ in range(N)]
tree={}

for _ in range(M):
    x,y,age=map(int,input().split())
    x,y=x-1,y-1
    if (x,y) not in tree:
        tree[(x,y)]=[age]
    else:
        tree[(x,y)].append(age)

cnt = 0
# K번 반복한다
for _ in range(K):
    # 정렬한다
    for key in tree:
        tree[key].sort()
    die = {}
    # 봄
    new_tree={}
    for x,y in tree:
        for i in range(len(tree[(x,y)])):
            age=tree[(x,y)][i]
            if arr[x][y]>=age:
                arr[x][y]-=age
                age+=1
                if (x, y) not in new_tree:
                    new_tree[(x, y)] = [age]
                else:
                    new_tree[(x, y)].append(age)
            else:
                if (x, y) not in die:
                    die[(x, y)] = [age]
                else:
                    die[(x, y)].append(age)
    tree={}
    tree=new_tree

    # 여름
    if die:
        for (x,y) in die:
            for age in die[(x,y)]:
                arr[x][y]+=age//2

    # 가을
    new_tree={}
    for (x, y) in tree:
        for age in tree[(x, y)]:
            if age%5==0:
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)):
                    ni,nj=x+di,y+dj
                    if 0<=ni<N and 0<=nj<N:
                        if (ni,nj) not in new_tree:
                            new_tree[(ni, nj)] = [1]
                        else:
                            new_tree[(ni, nj)].append(1)
            if (x,y) not in new_tree:
                new_tree[(x,y)] = [age]
            else:
                new_tree[(x,y)].append(age)
    tree={}
    tree=new_tree

    # 겨울
    for i in range(N):
        for j in range(N):
            arr[i][j]+=fill[i][j]

    cnt+=1

ans=0
for key in tree:
    ans+=len(tree[key])
print(ans)
'''