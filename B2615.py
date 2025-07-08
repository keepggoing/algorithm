'''
네 변에 다 0으로 패딩 후 5개씩 확인해봄 단, [i-1], [i+5]가 같은 수인지 아닌지 추가로 확인

틀린 이유: 가장 왼쪽에 있는 바둑알의 번호를 출력하는 거 !!!
반대방향 대각선은 시작점이 아니라 이동 후 마지막 바둑알의 위치인데 이걸 놓침
'''

# 행과 열 확인
def check(arr):
    m=-1
    for lst in arr:
        m+=1
        for i in range(1,16):
            cnt1 = 0
            cnt2 = 0
            for j in range(5):
                if lst[i+j]==1:
                    cnt1+=1
                elif lst[i+j]==2:
                    cnt2 += 1
                else:
                    break
            if cnt1==5 and lst[i-1]!=1 and lst[i+5]!=1:
                return 1,[m,i]
            elif cnt2==5 and lst[i-1]!=2 and lst[i+5]!=2:
                return 2,[m,i]
    else:
        return 0,[0,0]

# 대각선 확인
def check2(arr):
    for i in range(1,16):
        for j in range(1,16):
            cnt1=0
            cnt2=0
            for k in range(5):
                if arr[i+k][j+k]==1:
                    cnt1+=1
                elif arr[i+k][j+k]==2:
                    cnt2+=1
                else:
                    break
            if cnt1 == 5 and arr[i - 1][j - 1] != 1 and arr[i + 5][j + 5] != 1:
                return 1,[i,j]
            elif cnt2 == 5 and arr[i - 1][j - 1] != 2 and arr[i + 5][j + 5] != 2:
                return 2,[i,j]

    # 반대 방향 대각선
    for i in range(1,16):
        for j in range(19,4,-1):
            cnt1 = 0
            cnt2 = 0
            for k in range(5):
                if arr[i+k][j-k]==1:
                    cnt1+=1
                elif arr[i+k][j-k]==2:
                    cnt2+=1
                else:
                    break
            if cnt1 == 5 and arr[i - 1][j + 1] != 1 and arr[i + 5][j -5] != 1:
                return 1, [i+4, j-4]
            elif cnt2 == 5 and arr[i - 1][j + 1] != 2 and arr[i + 5][j -5] !=2:
                return 2, [i+4, j-4]
    return 0,[0,0]

# 0으로 패딩
arr=[[0]*21]+[[0]+list(map(int,input().split()))+[0] for _ in range(19)]+[[0]*21]
arr_t=list(map(list,zip(*arr)))

a,b=check(arr)
c,d=check(arr_t)
e,f=check2(arr)

if a != 0:
    print(a)
    print(*b)
elif c != 0:
    print(c)
    print(*d[::-1])
elif e != 0:
    print(e)
    print(*f)
else:
    print(0)