''' 테트로미노 (1/74) / 2025-02-26 / 체감 난이도 : 골드 4-5
소요 시간 : 1시간 14분 / 시도 : 1회 / 실행 시간 : 420ms / 메모리 : 117328KB

[타임라인]
1. 문제 이해 & 구상 & sudo code 작성 (1시간)
2. 구현 (sudo code를 많이 적어놔서 거의 옮겨적기) (13분)

[디버깅 내역]
1. sm = sum((sum(row[j:j + 2]) for row in arr[i:i + 3]))
위 코드를 sm = (sum(row[j:j + 2]) for row in arr[i:i + 3]) 이렇게 작성, 즉 sum 하나를 빼먹어서
"TypeError: unsupported operand type(s) for -: 'generator' and 'int'"
-> sm을 찍어보니까 <generator object ~> 가 나오길래 다시 코드를 살펴봄
결론 : 이렇게 코드를 간결하게 쓸 때는 더 조심해야 한다

[구상]
모양 별로 종이에 그려가면서 생각
인덱스 가지고 옮겨가며 하는 방법 말고는 떠오르는게 없는데? 또또 무식하게..
너무 많아서 시간초과 나려나? 누적합 써야돼..? 일단 해보자
해보다보니 규칙성이 있네? 그냥 arr_t를 사용하면 반복 작업 안 해도 되겠다

[구현]
구현 과정에서 arr_t를 써서 간결하게
three() 함수는 그냥 하나하나 이미 적어놔서 굳이 안 고쳤다

[마지막 체크 포인트]
전치 행렬을 쓴 만큼 N,M index error가 날까봐 그 부분을 중점적으로 봤다

[후기]
이 문제는 구상에서 실수하면 디버깅 하기 너무 힘들겠다고 생각함
그래서 구상 & sudo code 작성을 최대한 꼼꼼히 하려고 하니까 구현 시간이 정말 별로 안 걸리는 구나 ( 이런 느낌을 처음 느껴봤다 )

근데 여전히 시험이 시작되면 제일 안전하게 다 ~ 해보는 무식한 풀이 과정만 생각난다..
나 스스로가 기발한 생각을 시도하려는 노력 조차 안 한다

그리고 처음에 문제 이해 잘못..한 부분 있는데
'회전이나 대칭을 시켜도 된다' => 회전, 대칭 중 한 번만 가능한건지 or 둘 다 해도 되는지
" or " 이니까 다 될 듯
'''

# 쭉 연결된 모양
def one():
    mx = -1

    # 행 별로 찾기
    for row in arr:
        for i in range(M - 3):
            mx = max(mx, sum(row[i:i + 4]))

    # 전치행렬 써서 열 별로 찾기
    # 이 부분은 코드가 간단해서 직접 N,M을 바꿔주었다
    for row in arr_t:
        for i in range(N - 3):
            mx = max(mx, sum(row[i:i + 4]))
    ans.append(mx)

# 정사각형 모양
def two():
    mx = -1
    for i in range(N - 1):
        for j in range(M - 1):
            temp = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
            mx = max(mx, temp)

    ans.append(mx)

# ㅗ 모양
# 이때까지만 해도 규칙성이 있는지 발견하지 못하고 하나 하나 작성
def three():
    mx = -1
    # ㅜ 모양
    for i in range(N - 1):
        for j in range(M - 2):
            temp = arr[i + 1][j + 1] + arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            mx = max(mx, temp)

    # ㅗ 모양
    for i in range(1, N):
        for j in range(M - 2):
            temp = arr[i - 1][j + 1] + arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            mx = max(mx, temp)

    # ㅏ 모양
    for i in range(N - 2):
        for j in range(1, M):
            temp = arr[i + 1][j - 1] + arr[i][j] + arr[i + 1][j] + arr[i + 2][j]
            mx = max(mx, temp)

    # ㅓ 모양
    for i in range(N - 2):
        for j in range(0, M - 1):
            temp = arr[i + 1][j + 1] + arr[i][j] + arr[i + 1][j] + arr[i + 2][j]
            mx = max(mx, temp)
    ans.append(mx)

# 나머지 두개의 모양
# 여기 구상하면서 규칙성이 있다는 사실을 깨달음
# 나머지 두개 모양은 모두 6개짜리 직사각형에서 2개씩 빼면 나옴
def four():
    global N,M
    mx=-1
    for i in range(0, N - 2):
        for j in range(0, M - 1):
            sm = sum((sum(row[j:j + 2]) for row in arr[i:i + 3]))
            tp1 = sm - arr[i][j] - arr[i + 1][j]
            tp2 = sm - arr[i + 1][j] - arr[i + 2][j]
            tp3 = sm - arr[i][j + 1] - arr[i + 1][j + 1]
            tp4 = sm - arr[i + 1][j + 1] - arr[i + 2][j + 1]
            tp5 = sm - arr[i][j] - arr[i + 2][j + 1]
            tp6 = sm - arr[i][j + 1] - arr[i + 2][j]
            mx = max(mx, tp1, tp2, tp3, tp4, tp5, tp6)

    # 어차피 이게 마지막 함수, 마지막 실행이니까 N,M을 바꿔준다
    N,M=M,N
    for i in range(0, N - 2):
        for j in range(0, M - 1):
            sm = sum((sum(row[j:j + 2]) for row in arr_t[i:i + 3]))
            tp1 = sm - arr_t[i][j] - arr_t[i + 1][j]
            tp2 = sm - arr_t[i + 1][j] - arr_t[i + 2][j]
            tp3 = sm - arr_t[i][j + 1] - arr_t[i + 1][j + 1]
            tp4 = sm - arr_t[i + 1][j + 1] - arr_t[i + 2][j + 1]
            tp5 = sm - arr_t[i][j] - arr_t[i + 2][j + 1]
            tp6 = sm - arr_t[i][j + 1] - arr_t[i + 2][j]
            mx = max(mx, tp1, tp2, tp3, tp4, tp5, tp6)
    ans.append(mx)

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
arr_t = list(map(list, zip(*arr)))
ans=[]

# 함수 실행
one()
two()
three()
four()

# max값 출력
print(max(ans))