'''
문제
소수를 유난히도 좋아하는 창영이는 게임 아이디 비밀번호를 4자리 ‘소수’로 정해놓았다. 어느 날 창영이는 친한 친구와 대화를 나누었는데:

“이제 슬슬 비번 바꿀 때도 됐잖아”
“응 지금은 1033으로 해놨는데... 다음 소수를 무엇으로 할지 고민중이야"
“그럼 8179로 해”
“흠... 생각 좀 해볼게. 이 게임은 좀 이상해서 비밀번호를 한 번에 한 자리 밖에 못 바꾼단 말이야. 예를 들어 내가 첫 자리만 바꾸면 8033이 되니까 소수가 아니잖아. 
여러 단계를 거쳐야 만들 수 있을 것 같은데... 예를 들면... 1033 1733 3733 3739 3779 8779 8179처럼 말이야.”
“흠...역시 소수에 미쳤군. 그럼 아예 프로그램을 짜지 그래. 네 자리 소수 두 개를 입력받아서 바꾸는데 몇 단계나 필요한지 계산하게 말야.”
“귀찮아”
그렇다. 그래서 여러분이 이 문제를 풀게 되었다. 입력은 항상 네 자리 소수만(1000 이상) 주어진다고 가정하자. 
주어진 두 소수 A에서 B로 바꾸는 과정에서도 항상 네 자리 소수임을 유지해야 하고, ‘네 자리 수’라 하였기 때문에 0039 와 같은 1000 미만의 비밀번호는 허용되지 않는다.

입력
첫 줄에 test case의 수 T가 주어진다. 다음 T줄에 걸쳐 각 줄에 1쌍씩 네 자리 소수가 주어진다.

출력
각 test case에 대해 두 소수 사이의 변환에 필요한 최소 회수를 출력한다. 불가능한 경우 Impossible을 출력한다.
'''
#132520kb	376ms
from collections import deque
def get_candi(x):#한 자리씩 0~9 대입하고 소수인 것 찾기
    candi=set()
    for e in range(4):
        for num in range(10):
            tmp=x[:e]+str(num)+x[e+1:]
            if not check[int(tmp)]: continue
            if e==0 and num==0: continue
            candi.add(tmp)
    return candi

#소수 구하기
check=[1 for _ in range(10000)]
check[0]=0
check[1]=0
for i in range(2,10000):
    if not check[i]:continue
    for j in range(i*i,10000,i):
        check[j]=0
        
T=int(input())
while T:
    T-=1
    ans=0
    A,B=input().split()

    if A==B:
        print(0)
        continue

    que=deque()
    done=set()
    for a in get_candi(A):
        que.append((a,1))
        done.add(a)

    while que:
        target,cnt=que.popleft()
        if target==B:
            ans=cnt
            break
        for c in get_candi(target):
            if c not in done:
                que.append((c,cnt+1))
                done.add(target)

    print("Impossible" if ans==0 else ans)


#127672kb	248ms
#코드 정리
from collections import deque
def get_candi(x):#한 자리씩 0~9 대입하고 소수인 것 찾기
    candi=set()
    for e in range(4):
        for num in range(10):
            tmp=x[:e]+str(num)+x[e+1:]
            if not check[int(tmp)] or tmp in done: continue
            if e==0 and num==0: continue
            candi.add(tmp)
            done.add(tmp)#done 여기서 추가
    return candi

#소수 구하기
check=[0,0]+[1 for _ in range(2,10000)]
for i in range(2,10000):
    if not check[i]:continue
    for j in range(i*i,10000,i):
        check[j]=0

T=int(input())
while T:
    T-=1
    ans=0
    A,B=input().split()

    if A==B:
        print(0)
        continue
    done = set()
    que=deque((a,1) for a in get_candi(A))
    while que:
        target,cnt=que.popleft()
        if target==B:
            ans=cnt
            break
        for c in get_candi(target):
            que.append((c,cnt+1))

    print("Impossible" if ans==0 else ans)