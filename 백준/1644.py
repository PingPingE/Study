'''
문제)
하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.

3 : 3 (한 가지)
41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
53 : 5+7+11+13+17 = 53 (두 가지)
하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다.
7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다.
또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.

자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 4,000,000)

출력)
첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.
'''
N = int(input())
check = [0 for _ in range(N+2)]
prime = []
prime_ap = prime.append
tmp_sum=0
s,e = 0,0
cnt =0
if N <2:
    print(0)
else:
    #소수 구하기
    #소수 구하면서 중간중간에도 연산하면 222552kb	720ms
    #그냥 소수 다 구하고 연산하면 	222424kb	616ms
    for i in range(2, N+1):
        if check[i]:
            continue
        prime_ap(i)
        # if s>e:
        #     break
        # if tmp_sum > N:
        #     tmp_sum -= prime[s]
        #     s+=1
        # else:
        #     tmp_sum += prime[e]
        #     e+=1
        # if tmp_sum == N:
        #     cnt += 1

        for j in range(i*i,N+1,i):
            check[j] = 1
    while s<=e and  e<=len(prime):
        if tmp_sum > N:
            tmp_sum -= prime[s]
            s+=1
        elif e == len(prime):
            break
        else:
            #elif빼고 여기 안에 넣으면
            #222424kb	660ms
            # if e == len(prime):
            #     break
            tmp_sum += prime[e]
            e+=1
        if tmp_sum == N:
            cnt += 1
    print(cnt)
