def check(lst):
    # 길이 D에 대해서 확인
    pivot=lst[0]
    cnt=1

    for j in range(1,D):
        if lst[j] == pivot:
            cnt+=1
            if cnt>=K:
                return 1
        else:
            if cnt>=K:
                return 1
            else:
                pivot=lst[j]
                cnt=1
    return 0

T=int(input())
for tc in range(1,T+1):
    D,W,K=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(D)]
    arr=list(map(list,zip(*arr)))   # 이제 행이 W, 열이 D 가 되었음

    def btk(select,idx,new,lst):
        global flag

        if select == cnt:
            # 이렇게 하면 new에 어떤 열을 고를지
            # lst에는 각각 어떤 막으로 변화시킬지 나와있음
            temp=[row[:] for row in arr]

            for k in range(len(new)):        # temp를 다 바꾸고 나서 다시 체크
                idx=new[k]
                for i in range(0,W):
                    temp[i][idx]=lst[k]

            for lst in temp:
                result = check(lst)
                if not result:
                    break
            else:
                flag=True
            return

        if flag:
            return

        for i in range(idx,D):
            for num in range(2):
                new.append(i)
                lst.append(num)
                btk(select+1,i+1,new,lst)
                new.pop()
                lst.pop()

    for cnt in range(0,D+1):
        flag=False
        btk(0,0,[],[])
        if flag:
            ans=cnt
            break

    print(f'#{tc} {ans}')