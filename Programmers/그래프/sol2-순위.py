from collections import defaultdict
def solution(n, results):
    m_result = {i:[set(),set()] for i in range(n)}#key: 선수 번호, value:[set(key선수가 이긴 선수), set(key선수가 진 선수)]
    ans = set()#순위를 매길 수 있는 선수(번호) 집합
    for i,j in results:
        m_result[i-1][0].add(j-1)
        m_result[j-1][1].add(i-1)
    if n<3: #어차피 경기결과는 1개 이상이므로 2명 이하까지는 무조건 알 수 있다.
        return n
    warn = 0 #while문 돌기 전 len(ans)값인 prev와 비교했을 때 증가하지 않았을 경우 경고
#여러번 돌려야 골고루 알 수 있음
    while warn <2: #경고는 1번까지만 
        m_res2 = defaultdict(list)
        prev = len(ans)
        for k,v in m_result.items():
            if k in ans:
                continue
            win_v = set()
            lose_v = set()
            for win in v[0]: #내가 이긴 선수와 붙어서 진 선수는 나도 이긴다
                w=set(i for i in m_result[win][0])
                win_v|=w
            for lose in v[1]: #나를 이긴 선수와 붙어서 이긴 선수는 나도 진다
                l = set(i for i in m_result[lose][1])
                lose_v |= l
            m_res2[k] = [win_v|v[0], lose_v|v[1]]
            if len(m_res2[k][0])+len(m_res2[k][1]) >= n-1: #내가 이기고 진 선수 집합의 크기가 n-1이상이면(즉, 다 알면) 결과를 알 수 있다.
                ans.add(k)
        if prev == len(ans): #이전 len(ans)과 비교
            warn += 1
        for k,v in m_res2.items(): #새로 추가된 정보 저장
            m_result[k] = v
    return len(ans)

정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.8MB)
테스트 2 〉	통과 (0.11ms, 10.8MB)
테스트 3 〉	통과 (0.17ms, 10.8MB)
테스트 4 〉	통과 (0.11ms, 10.7MB)
테스트 5 〉	통과 (1.76ms, 10.9MB)
테스트 6 〉	통과 (4.61ms, 11MB)
테스트 7 〉	통과 (23.65ms, 11.4MB)
테스트 8 〉	통과 (51.32ms, 13.8MB)
테스트 9 〉	통과 (64.35ms, 16.3MB)
테스트 10 〉	통과 (34.68ms, 17.5MB)

#-------굳이 없어도 되는거 삭제---------------------
def solution(n, results):
    if n<3:
        return n
    dic = {r:[set(),set()] for r in range(1,n+1)}
    ans = set()
    for w, l in results:
        dic[w][0].add(l)
        dic[l][1].add(w)
        
    warn = 0
    while warn <2:
        tmp = len(ans)
        for k,v in dic.items():
            win_s = set()|v[0]
            lose_s = set()|v[1]
            for win in v[0]:
                win_s = dic[win][0]|win_s
            for lose in v[1]:
                lose_s = dic[lose][1]|lose_s
            if len(win_s) + len(lose_s) == n-1:
                ans.add(k)
            dic[k] = [win_s, lose_s]
        if tmp==len(ans):
            warn += 1
    return len(ans)

정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.9MB)
테스트 2 〉	통과 (0.11ms, 10.7MB)
테스트 3 〉	통과 (0.15ms, 10.8MB)
테스트 4 〉	통과 (0.09ms, 10.7MB)
테스트 5 〉	통과 (1.93ms, 10.9MB)
테스트 6 〉	통과 (3.55ms, 11.1MB)
테스트 7 〉	통과 (22.83ms, 11.3MB)
테스트 8 〉	통과 (48.88ms, 13.7MB)
테스트 9 〉	통과 (64.67ms, 16.2MB)
테스트 10 〉	통과 (50.82ms, 17.6MB)