'''
1. 다 틀린 답으로 내보기
2. 하나만 틀리게 내보기
3. 중간 검증 꼬꼮
### 2차 풀이 미완

[ 코드트리-백준 기출문제 매칭 ]
3/31
보도블럭	경사로

4/1
생명과학부 랩 인턴	낚시왕
종전	게리맨더링 2

4/2
윷놀이 사기단	주사위 윷놀이
2차원 테트리스	모노미노도미노 2
술래잡기 체스	청소년 상어
승자독식 모노폴리	어른 상어
자율주행 전기차	스타트 택시

4/3
회전하는 빙하	마법사 상어와 파이어스톰
놀이기구 탑승	상어 초등학교
색깔 폭탄	상어 중학교

4/4
나무 타이쿤	마법사 상어와 비바라기
미로 타워 디펜스	마법사 상어와 블리자드
정육면체 한번 더 굴리기	주사위 굴리기 2
냉방 시스템	온풍기 안녕!
팩맨	마법사 상어와 복제
Sam의 피자학교  어항정리

[ 백준에만 있는 문제들 ]
4/5
뱀
큐빙

[ 최근 기출 ]
메두사와 전사들
미지의 공간탈출

4/6
마법의 숲 탐색
고대 문명 유적 탐사
루돌프의 반란
왕실의 기사 대결

4/7
메이즈 러너
포탑 부수기
코드트리 빵
싸움땅

4/8
나무박멸
꼬리잡기놀이
예술성
술래잡기

# ============================================================================================
### 2차 풀이 완

[ 백준 실버 난이도 문제들]
바이러스 실험 - 시험 감독
외주 수익 최대화하기 - 퇴사
조삼모사 - 스타트와 링크
연산자 배치하기 - 연산자 끼워넣기

[ 코드트리-백준 기출문제 매칭 ]
2개의 사탕	구슬 탈출 2
정육면체 굴리기	주사위 굴리기
2048 게임	2048 (Easy)
테트리스 블럭 안의 합 최대화	테트로미노
자율주행 자동차	로봇 청소기
방화벽 설치하기	연구소
돌아가는 팔각 의자	톱니바퀴
디버깅	사다리 조작
드래곤 커브	드래곤 커브
병원 거리 최소화하기	치킨 배달
토스트 계란틀	인구 이동
바이러스 실험	나무 재테크
전투 로봇	아기 상어
시공의 돌풍	미세먼지 안녕!
격자 숫자 놀이	이차원 배열과 연산
바이러스 백신	연구소 3
이상한 윷놀이	새로운 게임 2
이상한 다트 게임	원판 돌리기
이상한 체스	감시
4/3
불안한 무빙워크	컨베이어 벨트 위의 로봇
원자 충돌	마법사 상어와 파이어볼
청소는 즐거워	마법사 상어와 토네이도
# =============================================================================

### 루틴
[1] 구상 ( 문제 이해, 자료구조 선택, 시간복잡도 계산 )
- 이해가 안 되는 부분은 손으로 적으면서 정리
- 찝찝한 부분은 시간이 걸리더라도 무조건 이해하고 가야함 ( 테케에서 주로 해결 가능 )
- 너무 종이 구상이 안 된다 -> 일단 들어가서 뚜드려보기 ( 단, 생각났으면 다시 종이로 )
- 자료구조 선택한 뒤 문제 다시 읽으면서 조건을 다 반영 가능한 자료구조인지 확인하기
- 대략적인 시간복잡도 계산하기
- 중요한 조건이 있다면 따로 정리해두며 히든 테케 생각하기

[2] 구현

[3] 검증
- 문제 다시 읽으면서 & 주석쓰면서 코드 정리하기
- 엣지케이스 생각 및 엣지케이스 리스트 검토하기
- 체크리스트 검토하기


### 엣지케이스 리스트
- bfs 쓸 떄, 아예 bfs 돌지 않아도 되는 경우가 있는지?
- 함수 안 돌리고 처음부터 되는 경우 예외처리 랬는지?

### 체크리스트
- 나누기 연산 있을 시 zero division 
- 갱신 안 됐을 때 초기값이 아니라 -1로  바꿔서 출력했는지?
- new_arr을 arr을 복사했는지 , 아님 빈 껍데기를 만드는 건지 유의
빈 껍데기일 떄는 다른 값 다 잘 들어가는지?
- (아기상어) 처음에 몬스터 있었던 곳 결국 빈칸이 되니까 초기에 빈칸으로 만들어줘야함
- 등호 포함?
- temp로 복사해서 배열 가지고 갔을 떄 다른 이름으로 받았다면 원래 배열 이름으로 하지 않도록 조심..
- 튜플 튜플 비교 잘 하고 있는지? 튜플 <-> 숫자 비교하고 있진 않은지?
- 범위 밖 체크 해줬는지?
- for mul in range(1,8) 을 range 빼먹어서 1이랑 8만 확인
- 백트래킹할 때 자꾸 i+1로 해야하는데 idx+1로 쓰는 실수를 함
- 내가 구하는 ans가 뭔지, mx가ㅏ 뭔지, 확실히 잘 생각하고 가야함
### 3차 풀이
- 이차원 배열과 연산 ( 딕셔너리에서의 sort, sum으로 펼치기 )
- 인구 이동
- 감시



'''
'''
[1] 실수한 점
1. 하드코딩 잘못 옮겨적음
2. bfs에서 amount == 1 됐을 때 중단하는 코드 빠짐
bfs에서 큐에 좌표 외 다른 값도 같이 넣고, 그 값이 종료조건이 될 때 자주 누락함 **

-> 둘다 자주 하는 실수, 체크리스트 추가하기

[2] 배울점
1. " 두 좌표의 대소 비교 후 큰 값에서 차이만큼 빼고, 작은 값에서 차이만큼 더하고 " 이 부분 구현 방법 두가지 있음
(1) 모든 좌표에서 우,하만 보기 (2) 모든 좌표에서 네방향 다 보지만 내가 클 때만 처리

2. 방향별 딕셔너리 만들어서 정해진 방향대로 bfs에서 보는 로직
'''
'''
[1] 실수한 점
1. remove(0) 하면 모든 0이 지워지는 거 아님

2. 아래처럼 코드를 쓴다면 값이 다를 때만 처리를 해주기 때문에 마지막 pivot과 cnt는 반영이 안됨
-> 리스트를 앞에서 하나씩 비교할 때 마지막 값도 잘 처리되는지 확인하기

for i in range(1,len(lst)):
    if lst[i] == pivot:
        cnt+=1
    else:
        if cnt >= 4:
            flag=True
            score+=pivot*cnt
            for j in range(i-1,i-1-cnt,-1):
                lst[j]=0
        pivot=lst[i]
        cnt=1

3. len(lst)라고 써야하는데 아예 관계 없는 N이라고 씀
-> 마지막 검토할 때 모든 변수 하나하나 의미 생각하면서 잘 썼는지 검토하기

-> 2,3번 체크리스트 추가하기

[2] 배울점
1. 내 달팽이 코드에는 flag 2번 확인해야 최종적으로 나갈 수 있는 거 잊지말기
2. 리스트 앞에서 하나씩 볼 때 마지막에 변수에 남은 값 처리해줘야 하는 거 2048 에서도 주의해야할 부분이였음
'''
''' 2차 풀이
[0] 타임라인
구상 (15분)
구현 (10분)
디버깅 (10분)

[1] 실수한 점
1. 방향 딕셔너리 잘못 쓰는 실수 드디어 나옴 -> 체크리스트 추가하기
2. 특수 영양제 투입한 거는 제외해야하는데 안함 ( 문제 조건 누락 )
3. 틀린 건 아니지만 아래처럼 하면 반복문에서 계속 set으로 바꿈 위에서 한번만 바꿔주면 됨

    new_nut=[]
    for i in range(N):
        for j in range(N):
            if arr[i][j]>=2 and (i,j) not in set(nut):
                arr[i][j]-=2
                new_nut.append((i,j))

    nut=new_nut

[2] 배울점
1. 이 풀이 이후로 간격 맞춰 출력할 때 아래 코드 외워서 사용할 거임
for row in arr:
    print(''.join(f'{x:4}' for x in row))

'''
'''
[1] 실수한 점
1. pi,pj=i,j 로 해야하는데 pi,pj=20,20 으로 bfs를 시작함
-> bfs 할 때 주의할 점, 시작하는 값도 비교되는지 꼭 확인하기

2. 음수 튜플 비교에서 실수함
-> 음수 튜플 비교할 때 실제 값과 비교시 사용하는 값이 다르니 주의해서 확인하기

-> 모두 체크리스트 추가하기

[2] 배울점
1. 중력 코드 정리하기
def gravity():
    # 모든 열을 볼거야
    for j in range(0,N):
        # 행 밑에서 부터 볼 건데 일단 포인터 처음엔 맨 마지막 가리키고 있을 거야
        pointer=N-1
        for i in range(N-1,-1,-1):
            if arr[i][j] == -1:         # 못 가는 곳이 나와? 그럼 그 위로 포인터를 올려
                pointer=i-1
            elif 0<=arr[i][j]<=M:       # 만약 옮겨야 할게 나왔어
                if pointer != i:        # 포인터랑 가리키는 곳이 다를 때만
                    arr[pointer][j],arr[i][j]=arr[i][j],-2  # 포인터에 지금 내 값 넣고, 원래 내 자리는 빈곳으로
                pointer-=1              # 포인터 하나 올려주고

2. 회전 zip 코드 정리하기
- 90도 회전
arr=list(map(list,zip(*arr[::-1]))

- 반시계 90도 회전
arr=list(map(list,zip(*arr))[::-1]
'''
'''
[1] 실수한점
1. 깊은 복사, 얕은 복사
-> 체크리스트 추가하기
그때 그때 new_arr을 만들어주는 건 맞지만 arr = new_arr 이렇게 연결하고 아래에서 두 배열을 동시진행 처리할 때 사용하고 있었음
그러면 당연히 new_arr이 바뀔 때 arr도 같이 바뀜

2. 또 >0일때만 하는 건데 if문 안 걸어줌, 이 실수 꽤 많이 함

3. l==0 일 때 continue로 올려버림
이 경우엔 회전만 안 하고 녹이는 건 했어야 함
-> continue 쓸 때 아래 동작 다 안 하는 건지 다시 한번 생각하기

[2] 배운점
1. 인덱스 회전 최종 정리

for si in range(0,N,l):
    for sj in range(0,N,l):
        for i in range(l):
            for j in range(l):
                - 90도 회전
                new_arr[si+i][sj+j]=arr[si+l-1-j][sj+i]

                - 180도 회전
                new_arr[si+i][sj+j]=arr[si+l-1-i][sj+l-1-j]

                - 270도 회전 (반시계 90도)
                new_arr[si+i][sj+j]=arr[si+j][sj+l-1-i]

2. 격자를 자체를 회전하는게 아니라 격자에서 또 4등분 해서 시계 방향 회전

for si in range(0,N,l):
    for sj in range(0,N,l):
        for i in range(half):
            for j in range(half):   # 3 -> 1
                new_arr[si+i][sj+j]=arr[si+i+half][sj+j]
            for j in range(half,l): # 1 -> 2
                new_arr[si+i][sj+j]=arr[si+i][sj+j-half]    # arr에서 가져오는 거니까 뺴야지

        for i in range(half,l):
            for j in range(half):  # 4 -> 3
                new_arr[si + i][sj + j] = arr[si + i][sj + j+half]
            for j in range(half,l): # 2 -> 4
                new_arr[si + i][sj + j] = arr[si + i-half][sj+j]
'''
'''
[1] 실수한점
1. flag를 True로 두고 하고 있었음
2. "다른 격자에 이동한 먼지의 양을 모두 합한 것 " -> 격자 밖에 나간 것도 포함인데 아니라고 생각했음

[2] 배운점
1. 애매한 건 오픈테케로 검증, 확인하고 넘어가야함
'''
'''

[1] 실수한점
1. value 자체가 리스트인데 new_atom[key]=[value] 리스트를 한번 더 감쌌음
-> 리스트 한번 더 / 덜 씌우는 실수 종종함, print해서 눈으로 확인하기, 체크리스트 추가하기
'''
'''
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
'''2차 풀이
[0] 타임라인
구상 (45분)
구현 (50분)
검증 및 디버깅 (20분)

[1] 실수한점
1. global 선언 안해줌
-> 코드 중간 중간 검토하다가 오류 뜨면 무조건 적어두기, 같은 실수 여러번 했을 가능성이 높으니까
2. while문에서 break 하나 빼먹음
3. 루돌프 위치 그때 그때 업데이트해서 바꾸면 안 되는데 그렇게 함
4. 함수 이름이랑 같은 변수 이름 쓰면 안됨
5. p_arr에 초기화 하는 거 하나 빼먹음

[2] 배운점
1. 연쇄작용시 temp에다 넣어두고 하나씩 옮기는 방법
def interaction(temp, ni, nj, di, dj):
    global out
    while True:
        if 0 <= ni < N and 0 <= nj < N:
            if p_arr[ni][nj] == 0:
                p_loc[temp][2], p_loc[temp][3] = ni, nj
                p_arr[ni][nj] = temp
                break
            else:
                new_temp = p_arr[ni][nj]
                p_loc[temp][2], p_loc[temp][3] = ni, nj
                p_arr[ni][nj] = temp

                ni, nj = ni + di, nj + dj
                temp = new_temp

        else:  # 범위가 벗어나면 temp는 죽음
            p_loc[temp][1] = 1
            out -= 1
            break
'''