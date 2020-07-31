import sys
sys.setrecursionlimit(10**8) #필수
def find(dic, x):
    if x not in dic:
        dic[x] =x+1
        return x
    dic[x] = find(dic,dic[x])
    return dic[x]

def solution(k, room_number):
    dic = {}
    for e,r in enumerate(room_number):
        room_number[e] = find(dic,r)
    return room_number

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.7MB)
테스트 2 〉	통과 (0.04ms, 10.7MB)
테스트 3 〉	통과 (0.04ms, 10.8MB)
테스트 4 〉	통과 (0.11ms, 10.6MB)
테스트 5 〉	통과 (0.04ms, 10.7MB)
테스트 6 〉	통과 (0.05ms, 10.7MB)
테스트 7 〉	통과 (0.05ms, 10.8MB)
테스트 8 〉	통과 (0.04ms, 10.8MB)
테스트 9 〉	통과 (0.04ms, 10.7MB)
테스트 10 〉	통과 (0.04ms, 10.7MB)
테스트 11 〉	통과 (0.04ms, 10.7MB)
테스트 12 〉	통과 (0.05ms, 10.7MB)
테스트 13 〉	통과 (0.05ms, 10.7MB)
테스트 14 〉	통과 (0.05ms, 10.8MB)
테스트 15 〉	통과 (0.07ms, 10.7MB)
테스트 16 〉	통과 (0.09ms, 10.7MB)
테스트 17 〉	통과 (0.09ms, 10.8MB)
테스트 18 〉	통과 (0.18ms, 10.7MB)
테스트 19 〉	통과 (0.30ms, 10.8MB)
테스트 20 〉	통과 (0.36ms, 10.8MB)
테스트 21 〉	통과 (0.61ms, 11MB)
테스트 22 〉	통과 (0.70ms, 11MB)
테스트 23 〉	통과 (0.53ms, 10.9MB)
테스트 24 〉	통과 (0.76ms, 11MB)
테스트 25 〉	통과 (0.05ms, 10.7MB)
테스트 26 〉	통과 (0.08ms, 10.8MB)
효율성  테스트
테스트 1 〉	통과 (351.85ms, 311MB)
테스트 2 〉	통과 (387.14ms, 313MB)
테스트 3 〉	통과 (360.25ms, 312MB)
테스트 4 〉	통과 (320.97ms, 313MB)
테스트 5 〉	통과 (140.42ms, 315MB)
테스트 6 〉	통과 (369.78ms, 314MB)
테스트 7 〉	통과 (382.26ms, 315MB)
'''
'''
dic을 전역변수로 선언했을 때

효율성 테스트
테스트 1 〉	통과 (454.28ms, 312MB)
테스트 2 〉	통과 (422.59ms, 312MB)
테스트 3 〉	통과 (402.46ms, 312MB)
테스트 4 〉	통과 (353.29ms, 312MB)
테스트 5 〉	통과 (165.79ms, 315MB)
테스트 6 〉	통과 (469.78ms, 314MB)
테스트 7 〉	통과 (478.87ms, 316MB)
'''
#다른 사람 코드 참고 (재귀X)
def solution(k, room_number):
    dic= {}
    answer = []
    for r in room_number:
        n= r
        #거쳐온 노드 표시
        visit =[n]#set보다 빠름
        while n in dic:
            n=dic[n] #n 갱신
            visit.append(n)
        answer.append(n)
        for v in visit:#거쳐온 노드들 모두 갱신
            dic[v] = n+1
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.7MB)
테스트 2 〉	통과 (0.04ms, 10.7MB)
테스트 3 〉	통과 (0.04ms, 10.7MB)
테스트 4 〉	통과 (0.10ms, 10.7MB)
테스트 5 〉	통과 (0.07ms, 10.7MB)
테스트 6 〉	통과 (0.05ms, 10.7MB)
테스트 7 〉	통과 (0.05ms, 10.6MB)
테스트 8 〉	통과 (0.04ms, 10.6MB)
테스트 9 〉	통과 (0.04ms, 10.6MB)
테스트 10 〉	통과 (0.04ms, 10.6MB)
테스트 11 〉	통과 (0.04ms, 10.6MB)
테스트 12 〉	통과 (0.05ms, 10.7MB)
테스트 13 〉	통과 (0.05ms, 10.7MB)
테스트 14 〉	통과 (0.05ms, 10.6MB)
테스트 15 〉	통과 (0.11ms, 10.7MB)
테스트 16 〉	통과 (0.09ms, 10.6MB)
테스트 17 〉	통과 (0.10ms, 10.7MB)
테스트 18 〉	통과 (0.18ms, 10.8MB)
테스트 19 〉	통과 (0.29ms, 10.7MB)
테스트 20 〉	통과 (0.36ms, 10.7MB)
테스트 21 〉	통과 (0.64ms, 11MB)
테스트 22 〉	통과 (0.73ms, 11MB)
테스트 23 〉	통과 (0.57ms, 10.8MB)
테스트 24 〉	통과 (0.78ms, 10.9MB)
테스트 25 〉	통과 (0.05ms, 10.6MB)
테스트 26 〉	통과 (0.08ms, 10.7MB)
효율성  테스트
테스트 1 〉	통과 (524.15ms, 311MB)
테스트 2 〉	통과 (468.28ms, 313MB)
테스트 3 〉	통과 (458.32ms, 311MB)
테스트 4 〉	통과 (364.51ms, 311MB)
테스트 5 〉	통과 (160.40ms, 314MB)
테스트 6 〉	통과 (454.11ms, 313MB)
테스트 7 〉	통과 (530.12ms, 316MB)
'''
