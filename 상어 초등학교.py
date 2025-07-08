''' 2차풀이
[0] 타임라인
구상 (10분)
구현 (20분)
디버깅 (10분)

[1] 실수한점
1. 이번에도 음수 튜플 비교 실수
일단 pivot에 받고 (여기서 음수 붙이면 당연히 오류) 그 다음 음수 씌워서 넣어주기
    _,_,x,y=pivot
    arr[-x][-y]=n0

2. score가 양수일 때만 처리
-> 이렇게 0 이상일 때만 처리 if문 가끔 빼먹음, 체크리스트에 추가하기

    if score>0:
        ans+=10**(score-1)

[2] 배운점


'''

N=int(input())
arr=[[0]*N for _ in range(N)]       # 여기에는 학생의 인덱스가 들어감
peop=[set() for _ in range(N**2+1)]

for _ in range(N**2):
    n0,n1,n2,n3,n4= map(int,input().split())
    friend=set((n1,n2,n3,n4))
    peop[n0]=friend
    pivot=(-1,-1,-21,-21)
    # 전체 맵을 돌면서
    for i in range(N):
        for j in range(N):
            like=0
            empty=0
            for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj=i+di,j+dj
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] == 0:
                        empty+=1
                    elif arr[ni][nj] in friend:
                        like+=1
            if pivot<(like,empty,-i,-j) and arr[i][j]==0:
                pivot=(like,empty,-i,-j)

    _,_,x,y=pivot
    arr[-x][-y]=n0

    # ============================================

ans=0
for i in range(N):
    for j in range(N):
        idx=arr[i][j]
        score=0
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=i+di,j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] in peop[idx]:
                score+=1
        if score>0:
            ans+=10**(score-1)

print(ans)

'''상어 초등학교 (1/57) / 20250226 / 체감 난이도 : 골드 4-5
소요 시간 : 1시간 / 시도 : 1회 / 실행 시간 : 192ms / 메모리 : 112768KB

** 일단 굉장히 잘못된 방법으로 1시간을 보냈음을 미리 알립니다 ...
( 머리가 안 돌아가서 구상을 못했다
그래서 구상을 토대로 구현을 한 것이 아니라 디버깅 하면서 구현을 했다 )

[타임라인]
1. 문제 이해 (10분)
-> 꼼꼼히 안 해서 문제 이해 잘못했고, 구상도 안 하고 간거나 마찬가지다

2. 구현 (20분)
뭔 정신으로 했는지 모르겠다
머리는 생각을 안 하는데 그냥 손이 쓰고 있었다

3. 디버깅하며 다시 구현 (20분)
- 격자의 맨 가운데에 숫자가 계속 덮어씌워지는 문제가 발생
-> temp를 바깥으로 빼고 temp에도 확정된 값들은 넣어줬다
( temp의 용도가 그게 아닌데 그냥 냅다 숫자를 넣어버리니까 당연히 에러 )

- sort 할 때 기본이 내림차순인가 오름차순인가부터 .. 갑자기 헷갈리더니.. 오름차순으로 바꿔버림
- 주어진 예제랑 비교하면서 디버깅 하다가 문제 이해를 잘못했다는 사실을 깨달음
-> [1] 단계가 안 되면 [1] 단계 후보 중 [2] 단계를 고려해야 하는데, 전체 중에서 [2] 를 구했다

[디버깅 내역]
1. 문제를 잘못 이해했다
2. 머리를 안 쓰니까 오름차순, 내림차순이 뭔지도 헷갈렸다
그래서 정렬할 때 - 붙였다 뗐다 했다..
3. 3차원 배열을 썼는데 마지막 인덱스 지정을 안 해줘서 오류 난 적이 5번은 있었다

[구상]
0으로 표시되어있는 곳은 아무도 앉지 않은 곳
내가 좋아하는 애 있으면 [여기에,+1] 0이면 [,여기에 +1]

[구현]

[마지막 체크 포인트]
검토 안 했다..

[후기]
오늘 문제를 대한 태도, 풀이 모두 총체적 난국이다
근데 일부로 그런 건 아니고 머리가 안 돌아가서 이렇게라도 한 거다 .. 컨디션이 안 좋다고 생각하진 않았는데 왜일까

뇌가 일을 안 해서.. 화장실 다녀와서 세수 한 번 하고 구상 제발 구상하자고 다짐했지만 또 안 됐다
그래서 포기하고 디버깅하면서 코드 짰다..

어떻게 문제를 풀어나가야 성공적인지 정답은 안다 근데 그게 안 되는 컨디션일 땐 어떻게 해야하는지 아직도 잘 모르겠다 ..
꾸역꾸역 구상을 해보려고 노력하는게 맞는지, 포기하고 지금처럼 디버깅하면서 코드를 짜야하는지

조금 더 생각해보고 질문도 한 후에 결론을 내야겠다
'''

N=int(input())
final=[[0]*N for _ in range(N)]
LIKE=[[] for _ in range (N**2+1)]

for _ in range(N**2):
    temp = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    pivot,a,b,c,d=map(int,input().split())
    LIKE[pivot].append(a)
    LIKE[pivot].append(b)
    LIKE[pivot].append(c)
    LIKE[pivot].append(d)

    like=set()
    like.add(a)
    like.add(b)
    like.add(c)
    like.add(d)

    for i in range(N):
        for j in range(N):
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj=i+di,j+dj
                if 0<=ni<N and 0<=nj<N:
                    if final[ni][nj]==0:
                        temp[i][j][1]+=1
                    elif final[ni][nj] in like:
                        temp[i][j][0]+=1

    mx1=-1

    # [1]번 구현
    for i in range(N):
        for j in range(N):
            if final[i][j] == 0 :
                if temp[i][j][0] > mx1:
                    seat1 = []
                    mx1=temp[i][j][0]
                    seat1.append((i,j))
                elif temp[i][j][0] == mx1:
                    seat1.append((i,j))

    #print(mx1,mx2)
    #print(seat1)
    #print(seat2)

    mx2=-1
    if len(seat1) ==1:
        final[seat1[0][0]][seat1[0][1]]=pivot
    else:
        # 1에서 나온 seat들 중에서 좋아하는 애 많은 거로
        for i,j in seat1:
            if temp[i][j][1] > mx2:
                seat2 = []
                mx2 = temp[i][j][1]
                seat2.append((i, j))
            elif temp[i][j][1] == mx2:
                seat2.append((i, j))

        if len(seat2) ==1:
            final[seat2[0][0]][seat2[0][1]] = pivot
        else:
            # 이것도 아니면 행, 열에 따라서 배정하면 된다
            seat2=sorted(seat2,key=lambda x:(x[0],x[1]))
            final[seat2[0][0]][seat2[0][1]] = pivot

# 인접한 칸에 앉은 좋아하는 학생 수 구하기
like=[[0]*N for _ in range(N)]
ans=0
for i in range(N):
    for j in range(N):
        count=0
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=i+di,j+dj
            if 0<=ni<N and 0<=nj<N and final[ni][nj] in LIKE[final[i][j]]:
                count+=1
        if count == 1:
            ans+=1
        elif count == 2:
            ans+=10
        elif count ==3:
            ans+=100
        elif count == 4:
            ans+=1000

print(ans)