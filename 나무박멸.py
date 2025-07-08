'''2차풀이
[0] 타임라인
구상 (20분)
구현 (45분)
디버깅 (12분)

[1] 실수한점
1. new_arr[x][y]+=amount 에서 +를 빠뜨림
-> 종종 실수함, += 인지 =인지 확인, 체크리스트 추가하기

2. 또 음수 튜플비교 실수

3. C년 지속해서 C+1년에 사라지면 C+1로 저장했어야함
-> 이렇게 몇년까지 지속, 몇번째 턴까지 지속 등등 주의해서 확인, 체크리스트 추가하기

4. 변수 잘못 작성
-> 변수 체크는 기본

[2] 배운점
1. zero division 엣지케이스 생각하기

'''
def my_print():
    print(year)
    print("=====")

    for row in arr:
        print(*row)

    print("====")

    for row in kill:
        print(*row)

    print("=====")


# 격자의 크기 N, 박멸이 진행되는 년수 M, 제초제 확산범위 K, 제초제가 남아있는 년수 C
N,M,K,C=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
kill=[[0]*N for _ in range(N)]
ans=0

for year in range(M):

    # [0] 제초제 하나씩 깍아줘 0보다 클 때만
    for i in range(N):
        for j in range(N):
            if kill[i][j]>0:
                kill[i][j]-=1

    new_arr=[row[:] for row in arr]                     # 깊은 복사 했고

    for i in range(N):
        for j in range(N):
            if arr[i][j]>0:                             # 0보다 클 때만 봐도 돼 성장과 번식은
                tree_exist=0                            # 나무가 있는 수
                empty=[]                                # 벽, 다른 나무, 제초제 없는
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj=i+di,j+dj
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj]>0:               # 나무가 있다면
                            tree_exist+=1
                        if arr[ni][nj]==0 and kill[ni][nj]==0:  # 빈칸이고 제초제도 없어
                            empty.append((ni,nj))

                new_arr[i][j]+=tree_exist               # new에 더해주고
                if empty:                               # 빈곳이 있다면 (zero division 방지)
                    amount=new_arr[i][j]//len(empty)    # arr말고 new_arr에서 나눠야지
                    for x,y in empty:
                        new_arr[x][y]+=amount           # 더해주고

    arr=new_arr                                         # 바꿔주고
    # ======================================================
    pivot=(0,-20,-20)                             # 그냥 항상 큰거를 담을거야
    pivot_lst=[]
    for i in range(N):
        for j in range(N):
            if arr[i][j]>0:                     # 0보다 큰곳만 보면 됨
                cnt=arr[i][j]                   # 박멸되는 나무의 수
                lst=[(i,j)]                     # 제초제 뿌려지는 곳의 좌표
                for di,dj in ((-1,1),(-1,-1),(1,-1),(1,1)):
                    for mul in range(1,K+1):
                        ni,nj=i+di*mul,j+dj*mul
                        if ni<0 or ni>=N or nj<0 or nj>=N:      # 범위 나가면 그 di,dj 는 끝낼거고
                            break
                        if 0<=ni<N and 0<=nj<N:                 # 범위 안이면
                            if arr[ni][nj]==-1 or arr[ni][nj]==0:   # 벽이거나 나무가 아예 없는 칸이면
                                lst.append((ni,nj))                 # 제초제가 뿌려지긴 한데 그 후 바로
                                break
                            else:
                                cnt+=arr[ni][nj]
                                lst.append((ni,nj))
                if (cnt,-i,-j)>pivot:                                 # pivot보다 크면
                    pivot=(cnt,-i,-j)
                    pivot_lst=lst

    # 이제 제초제 뿌릴 곳이 pivot에 있을 것
    # 만약 없다면?
    #my_print()
    #print(pivot)
    if pivot_lst:
        ans+=pivot[0]
        for x,y in pivot_lst:
            kill[x][y]=C+1
            if arr[x][y]>0:
                arr[x][y]=0         # 빈 곳으로 만들어주고
    #my_print()

print(ans)

'''
[체감 난이도 & 총평]
골 2~3
하 .. 또 놓쳤다.. 앞으로 나오는 모든 객체 쭉 쓰고 모든 상황을 의심하며 체크리스트 만들기

<체크리스트>
- 나무 (최대? 없는 경우? 번식, 성장 못할 수 있나?)
- 제초제 (제초제 범위?, 아예 못뿌릴 수가 있나?)

[시간복잡도]
m년 동안 n^2 4번 -> 1000 x 400 x 4 ㄱㅊ

[주의할 점]
- k의 범위만큼 퍼진다 -> k는 1이상 20이하 k가 격자 밖으로 나간다면? 범위 체크 필요함
- 성장 번식 동시에
- 번식이 가능한 칸이 없으면 번식 안함 (zero division)
- 벽이 있거나 나무가 아예 없는 칸까지는 제초제 뿌려야대
- c년 만큼 남아있다가 c+1년째에 사라짐
- 제초제 못 뿌릴 수도 있ㄴㅔ..

[타임라인]
14:15 문제 이해 및 구상 완료
14:40 구현 완료
15:00 오픈테케 오류 수정 및 코드 검토 완료
15:20 코드 재검토 및 주의해야할 점 적기 완료
-> 제초제가 안 뿌려질 수 있는 거 고려 안 해서 틀림

[배운점 및 실수한점]
- mx 값보다 클 때 좌표 업데이트 안 해줘서 인덱스 에러
- zero division 에러
- new_arr을 arr로 써서 값 잘못 나옴
- 값 맞아도 출력 해보니 벽이 있거나 나무가 아예 없는 칸 바로 끝내버림 & c년에 바로 사라지면 안 되는 거 발견

[추가 TC]
- 제초제 아예 못 뿌리는 경우 == 다 벽이야
5 1 1
0 0 0 0 0
0 -1 0 -1 0
0 0 30 0 0
0 -1 0 -1 0
0 0 0 0 0
ans : 30
'''

# 정답
ans=0
# 격자의 크기, 년수, 제초제 확산 범위, 제초제가 남아있는 년수
n,m,k,c=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]
nope=[[0]*n for _ in range(n)]

for _ in range(m):
    # [0] 이전 년도 냄새 하나 줄인다
    for i in range(n):
        for j in range(n):
            if nope[i][j]>0:
                nope[i][j]-=1

    # [1] 성장 & [2] 번식
    new_arr=[row[:] for row in arr]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and arr[i][j] != -1:
                cnt1=0   # 성장할 거
                cnt2=0   # 번식할 거
                need=[]  # 번식할 곳 좌표
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj=i+di,j+dj
                    if 0<=ni<n and 0<=nj<n:
                        if arr[ni][nj] != 0 and arr[ni][nj] != -1:
                            cnt1+=1
                        elif arr[ni][nj] == 0 and nope[ni][nj]==0:
                            cnt2+=1
                            need.append((ni,nj))
                new_arr[i][j] += cnt1
                if cnt2>0:
                    amount=new_arr[i][j]//cnt2  # 제로 디비전 에러
                    for x,y in need:
                        new_arr[x][y]+=amount

    arr=[row[:] for row in new_arr]

    # =============================================================================

    # [3] 제초제 뿌리기
    temp=[[0]*n for _ in range(n)]
    mx=0
    si,sj=20,20
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and arr[i][j] != -1:              # 나무가 있는 칸이면
                temp[i][j] += arr[i][j]                         # 일단 내꺼 더하고
                for di,dj in ((-1,-1),(-1,1),(1,-1),(1,1)):
                    for mul in range(1,k+1):                    # k 까지 전파하는데
                        ni,nj=i+di*mul,j+dj*mul
                        if ni<0 or ni>=n or nj<0 or nj>=n or arr[ni][nj] == -1 or arr[ni][nj] == 0:
                            break                               # 이건 여기서 끊어도 됨 어차피 없음
                        else:
                            temp[i][j]+=arr[ni][nj]
                if temp[i][j]>mx:
                    mx=temp[i][j]
                    si,sj=i,j
                elif temp[i][j]==mx:
                    if (i,j)<(si,sj):
                        si,sj=i,j

    # 이제 si,sj에는 제초제를 뿌려야하는 좌표가 나와있음 -> 아니지 없을 수도 있음
    # c+1년째에 사라져야 함
    if mx != 0:                 # 이거 빠뜨림 ;;
        ans+=arr[si][sj]
        arr[si][sj]=0
        nope[si][sj]=c+1
        for di,dj in ((-1,-1),(-1,1),(1,-1),(1,1)):
            for mul in range(1,k+1):
                ni,nj=si+di*mul,sj+dj*mul
                if ni<0 or ni>=n or nj<0 or nj>=n:
                    break
                elif arr[ni][nj] == -1 or arr[ni][nj] == 0:
                    nope[ni][nj]=c+1
                    break
                else:
                    ans+=arr[ni][nj]
                    arr[ni][nj]=0
                    nope[ni][nj]=c+1

print(ans)
