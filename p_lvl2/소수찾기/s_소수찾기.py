





"""
배운점:
1. list(문자열)을 할 경우, 각 단어가 분리되어 저장된다
2. map을 2번 중첩하여서 permutations => .join => int까지 한줄로 표현
3. |=은 in-place 연산자를 나타나는 걸로 or =로 이해했다
4. 소수판별은 set()에 저장된 값 중 가장 큰 수를 기준으로 구하고, 에토스테네 체를 사용한다
"""



from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
