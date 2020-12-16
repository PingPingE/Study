'''
문제 설명)
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 
아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.
삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

제한사항)
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.
'''

# T1: 15분 11초
# T2: 32분 47초(17분 36초) -> 중간에 이전 풀이 참고함
# T3: -
def solution(triangle):
    max_level = len(triangle)
    res = [[-1]*(len(_)+1) for _ in triangle] #해당 값을 선택했을 때의 최고값 저장
    def sol(r,c):#r: 레벨,  c: 해당 레벨에서의 index
        if r>= max_level:
            return 0
        if res[r][c]==-1:
            res[r][c] = triangle[r][c] + max(sol(r+1,c), sol(r+1,c+1))
        return res[r][c]
    return sol(0,0)

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (0.13ms, 10.2MB)
테스트 4 〉	통과 (0.47ms, 10.2MB)
테스트 5 〉	통과 (2.40ms, 10.4MB)
테스트 6 〉	통과 (0.98ms, 10.3MB)
테스트 7 〉	통과 (3.36ms, 10.5MB)
테스트 8 〉	통과 (0.77ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
테스트 10 〉	통과 (0.44ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (64.68ms, 18.4MB)
테스트 2 〉	통과 (50.55ms, 16.6MB)
테스트 3 〉	통과 (70.20ms, 19.5MB)
테스트 4 〉	통과 (65.41ms, 18.4MB)
테스트 5 〉	통과 (60.13ms, 17.8MB)
테스트 6 〉	통과 (74.10ms, 19.8MB)
테스트 7 〉	통과 (66.58ms, 19MB)
테스트 8 〉	통과 (55.77ms, 17.5MB)
테스트 9 〉	통과 (58.66ms, 17.9MB)
테스트 10 〉	통과 (68.89ms, 19.1MB)
'''