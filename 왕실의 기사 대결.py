''' 2차풀이
[0] 타임라인
구상 (20분)
구현 (40분)
디버깅 (1시간)
[1] 실수한점
1. 체스판 밖도 벽으로 간주합니다
-> 밖으로 나가게 못한다는 의미인데 잘못 생각함

2. 새로운 배열에 옮겨줘야지 안 그러면 문제 생김

3. 조건 누락 내 자신은 안 민다고 했음

4. 같은 거 두번 넣으면 안 되는데 계속 넣고 있음

5. new_arr에 고쳐줘ㅓ야하는데 그때그때 덮엌어우고 있음

[2] 배운점

'''

def my_print():
    print(p_loc)
    print(p_all)
    for row in p_arr:
        print("".join(f'{x:4}' for x in row))
    print("========")

# =============================================================================
# L은 체스판 길이, N은 기사 인원, Q는 명령 개수
L,N,Q=map(int,input().split())
# 체스판 정보가 0은 빈칸, 1은 함정, 2는 벽
arr=[list(map(int,input().split())) for _ in range(L)]

p_loc=[[]]  # 정보
p_all=[[] for _ in range(N+1)]  # 모든 좌표
p_arr=[[0]*L for _ in range(L)] # 표시
power=[0]*(N+1)   # 처음 체력

for idx in range(1,N+1):
    r,c,h,w,k=map(int,input().split())
    r,c=r-1,c-1
    p_loc.append([False,r,c,h,w,k])
    power[idx] = k
    for i in range(h):
        for j in range(w):
            p_arr[r+i][c+j]=idx
            p_all[idx].append((r+i,c+j))

# 상, 우, 하, 좌 순서
dic={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}


for _ in range(Q):
    idx,d=map(int,input().split())
    if p_loc[idx][0] == True:
        continue
    di,dj=dic[d]            # 가야하는 방향
    need=[idx]              # 움직여야하는 기사에 일단 명령 받은 애 넣고
    start=0                 # 봐야할 거 스타트 인덱스
    l=len(need)             # 여기까지 보면 돼
    flag=False              # 일단 플래그 펄스

    while True:             # 항상 참인 동안
        for i in range(start,l):  # 스타트부터 l까지 해서 일단 지금까지 꺼만 봐 (새로 추가된 거 말구)
            for x,y in p_all[need[i]]:  # 모든 좌표 볼건데
                ni,nj=x+di,y+dj
                if 0<=ni<L and 0<=nj<L: # 범위 내이고
                    if p_arr[ni][nj]!=0 and p_arr[ni][nj] != need[i] and p_arr[ni][nj] not in need:    # 만약 비지 않았어 누가 있어
                        need.append(p_arr[ni][nj])    # 그러면 얘도 또 연쇄적으로 봐야하지
                    elif arr[ni][nj]==2:        # 만약 벽이 있어
                        need=[]                 # 그럼 아무도 못옮겨
                        flag=True               # 플래그 바꾸고
                        break                   # 종료
                else:
                    need = []  # 그럼 아무도 못옮겨
                    flag = True  # 플래그 바꾸고
                    break  # 종료
            if flag:
                break
        if flag:
            break
        if l == len(need):
            break
        start=l
        l=len(need)

    # 이제 need에는 움직여야할 애가 있으니까 뒤에서부터 이동시켜줌
    if need:
        new_p_arr=[[0]*L for _ in range(L)]

        for i in range(len(need)-1,-1,-1):
            idx=need[i]
            new_all=[]
            cnt=0
            for x,y in p_all[idx]:
                ni,nj=x+di,y+dj
                if arr[ni][nj]==1:
                    cnt+=1
                new_all.append((ni,nj))
            if i==0:
                cnt=0
            # p_arr[ni][nj]=idx
            p_all[idx]=new_all
            # cnt에는 함정의 개수가
            flag,r,c,h,w,k=p_loc[idx]
            if k-cnt<=0:
                p_loc[idx][0]=True          # 아무것도 추가 안 하면 되는 거고
            else:                           # 괜찮다면
                p_loc[idx]=[False,r+di,c+dj,h,w,k-cnt]
                #print(idx,new_all)
                for x,y in new_all:
                    new_p_arr[x][y]=idx

        for idx in range(1,N+1):
            if idx not in need and p_loc[idx][0]==False:
                for x,y in p_all[idx]:
                    new_p_arr[x][y]=idx
        p_arr=new_p_arr
    #my_print()


ans=0
for idx in range(1,N+1):
    if p_loc[idx][0]==False:
        ans+=power[idx]-p_loc[idx][5]
print(ans)



'''
[체감 난이도 & 총평]
골 1
당황하즤마.. 어차피 시험에도 무조건 새로운 거 나올테니 당황하지말고 새로운 아이디어 내는 걸 두려워하즤마..
당황하니까 루틴이 무너지는 느낌? 차근 차근 아이디어 내기 ****

느무 힘들어서 테케로 틀린 부분 검증하려고 했던 스스로 반성해.... 오히려 디버깅 시간 늘어남
어차피 그거만으로 안 되고 로직 검토로 돌아오게 되어있잔하..

[시간 복잡도]
100번 반복하면서 x ( 기사 N명 반복할때 체스판 쭉 돈다고 하면 - 30 x 1600 )
48 x 10^5 ! ㄱㅊ

[타임라인]
1400 - 1440 구상
1440 - 1515 구현 ( 근데 더러워진 것 같아서 코드 삭제 )
1515 - 1550 재구현 완료 ( 오픈테케 완 )
1600 1차 제출 -> 인덱스 에러 ( 범위 밖 체크 안함 )
1600 - 1613 디버깅 후 2차 제출 -> 아직도 인덱스 에러 ( for문이 아니라 while문으로 해야했는데 )
1613 - 1630 디버깅 후 3차 제출 -> 틀렸습니다 ( 오타 )
1630 - 1730 오타로 1시간동안 디버깅 ( 말도 안됨 )

[배운점 및 실수한 점]
- 범위 나가는 걸 처리 안함 -> 이런 문제의 경우 패딩도 좋은 선택지
- for 문으로 하면 그때 그때 스택 길이를 계산해주면서 for문을 다시 돌거라고 생각했는데 아님
-> while문을 써야함
- stack[i]를 i라고 씀
-> 뭔가 코드에 자신이 없을 때 자꾸 코드를 읽는게 아니라 테케에 의존하려는 경향이 있음
운 좋아서 통과한 경우가 없다는 걸 이젠 알지 않니 ...?
절대로 그렇게 문제 맞을 수 없음 이 문제를 끝으로 이런짓 놉

'''

L,N,Q=map(int,input().split())                          # 체스판 크기, 기사 인원, 명령의 수
arr=[list(map(int,input().split())) for _ in range(L)]  # arr 맵에서는 함정, 벽만 체크
p_loc=[[False,-1,-1,-1,-1,-1]]                          # 인덱스번째 기사가 체스판에서 사라졌는지, r,c,h,w,k
p=[[0]*L for _ in range(L)]                             # 그 칸에 어떤 기사가 있는지 맵에 인덱스 표시
all=[[] for _ in range(N+1)]                            # 인덱스번째 기사의 모든 좌표 표시
init=[0]                                                # 초기 체력만 담는다

for idx in range(1,N+1):
    r,c,h,w,k=map(int,input().split())
    r,c=r-1,c-1
    p_loc.append([False,r,c,h,w,k])
    init.append(k)

    for i in range(r,r+h):
        for j in range(c,c+w):
            p[i][j]=idx                                 # 결국 기사에 대해서 p_loc,p,all 세개를 관리중
            all[idx].append((i,j))

# ====================================================================================================
dic={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}

for _ in range(Q):                                     # Q번의 반복동안
    i,d=map(int,input().split())
    if p_loc[i][0]==True:                              # 만약 체스판에 없는 기사라면 바로 다음 명령으로 !
        continue

    di, dj = dic[d]                                    # stack에는 자리를 옮겨야하는 기사의 인덱스가 들어감 명령 받은 사람부터 타고 타고 가면서 연쇄작용 당하는 사람 인덱스를 넣을 건데
                                                       # 막상 옮길 때는 뒤에서 부터 옮겨야 하니까 stack 자료구조를 선택 !
    stack=[i]                                          # 명령 받은 기사 인덱스 넣어주고

    flag=False                                         # 벽을 만났거나 범위를 나간다 = 못 민다 일 때 바로 나가기 위한 플래그
    i=0                                                # stack의 인덱스

    while i<len(stack):                                # i와 stack의 길이로 관리하면서 stack에 뭐가 더 추가됐다면 계속 while문 돈다 !
        for x, y in all[stack[i]]:                     # 그 인덱스 기사의 모든 좌표에 대해서 봐야함
            ni, nj = x + di, y + dj                    # 주어진 방향으로 하나 갔을 때
            if 0 <= ni < L and 0 <= nj < L and p[ni][nj] != 0 and p[ni][nj] != stack[i] and p[ni][nj] not in stack:     # 범위 내이고, 내가 아닌 누가 있고, 스택에 아직 추가하지 않았다면
                stack.append(p[ni][nj])                                                                                 # 스택에 추가

            if ni<0 or ni>=L or nj<0 or nj>=L or arr[ni][nj]==2:                            # 범위 밖을 나가거나 벽을 만나면 기사 아무도 못 가는 거야 -> 스택 비운다
                stack=[]
                flag=True                                                                   # 플래그 바꿔서 아예 중단
                break
        i+=1                                                                                # 인덱스 하나 더해서 while문으로
        if flag:
            break

    # ===============================================================================================================================

    while stack:                                                                  # 스택에 남은 애들은 옮겨도 되는 애들 !
        idx=stack.pop()                                                           # 하나씩 빼
        temp=[]                                                                   # temp 에는 새로운 좌표를 쭉 담을거고
        cnt=0                                                                     # cnt는 함정 몇개인지 세는 변수
        _,r,c,h,w,k=p_loc[idx]

        for x,y in all[idx]:
            ni,nj=x+di,y+dj
            temp.append((ni,nj))
            if arr[ni][nj] == 1:
                cnt+=1

        if cnt == 0:                                                               # 함정이 없다면
            p_loc[idx]=[_,temp[0][0],temp[0][1],h,w,k]                             # p_loc, all에 위치만 바꿔줘
            all[idx]=temp

        else:                                                                      # 함정이 있어서 데미지를 받을 건데
            if stack:                                                              # 스택이 남아있다 == 명령 받은 사람 아님
                if k-cnt>0:
                    p_loc[idx]=[_,temp[0][0],temp[0][1],h,w,k-cnt]
                    all[idx]=temp
                else:                                                              # 데미지 줘서 0이 되면 플래그 바꿔서 쫓아내
                    p_loc[idx]=[True,-1,-1,-1,-1,-1]
                    all[idx]=[]
            else:                                                                  # 스택이 안 남는다 == 첫번째 사람이니까 명령 받은 사람 == 피해 안 받아
                p_loc[idx]=[_,temp[0][0],temp[0][1],h,w,k]
                all[idx]=temp

    p = [[0] * L for _ in range(L)]                                                # 옮기고 나서 맵에도 반영
    for i in range(1,N+1):
        if p_loc[i][0]==False:                                                     # 맵에 있는 거만
            for x,y in all[i]:
                p[x][y]=i

# ===============================================================================================================================
ans=0
for i in range(1,N+1):
    if p_loc[i][0] == False:                                                       # 점수 계산도 살아남은 기사만
        ans+=init[i]-p_loc[i][5]                                                   # init이랑 차이 계산으로 구한다 !

print(ans)

