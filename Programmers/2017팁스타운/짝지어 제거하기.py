'''
짝지어 제거하기
문제 설명)
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 
먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 
그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 
이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 
문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 
성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

제한사항)
문자열의 길이 : 1,000,000이하의 자연수
문자열은 모두 소문자로 이루어져 있습니다.
'''

# 시간초과는 안나는데 일부 히든 테케가 틀린 코드
# 아마 제거 순서를 고려안해서?

from collections import deque
# 붙어있는 짝 찾아 제거하기
def sol(s):
    before = len(s)
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s[i], s[i + 1] = '', ''
            i += 2
        else:
            i += 1

    return (len(s) != before, ''.join(s))


# 문자열이 남아있는지
def check(s):
    if len(s) == 0:
        return True
    return False


def solution(s):
    que = deque([s])
    while que:
        q = que.popleft()
        if check(q):
            return 1

        diff, new_s = sol(list(q))

        if not diff:
            continue

        que.append(new_s)

    return 0