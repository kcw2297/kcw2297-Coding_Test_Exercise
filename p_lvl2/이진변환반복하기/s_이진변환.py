



"""
사용한 논리:
while문을 이용해서 s가 1이 될 때까지 반복한다
코드 가독성과 효율성면에서 훨씬 낫다
"""


def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1 # 반복횟수
        num = s.count('1')
        b += len(s) - num # 제거한 0의 개수
        s = bin(num)[2:] # 이진수로 변환
    return [a, b]



"""
사용한 논리:
위의 논리와 같지만 추가로 Counter 클래스를 사용했다
Counter를 활용하면 동일한 문자를 dict형태로 개수를 세서 저장한다
"""

def solution(s):
    from collections import Counter
    cnt, zero = 0, 0
    while s != '1':
        cnt += 1
        counter = Counter(s)
        zero += counter['0']
        s = bin(counter['1'])[2:]
    return [cnt, zero]