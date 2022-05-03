

"""
사용한 논리:
자릿수에 따른 숫자의 변화 규칙이 존재

5를 곱하는 것은 자리수별로 반복되는 횟수이며
1을 더하는 것은 빈칸을 의미한다
"""
def solution(word):
    char = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = len(word) # A를 0으로 두었기 때문에 길이로 초기화 필요
    re = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1 # 781
    

    for i in word:
        answer += re * char[i] # 첫 문자가 무슨 글자로 시작하는지
        re = (re - 1) // 5
    return answer  


"""
사용한 논리:
수학적 논리가 들어있는 문제로 예상했는데,
등비수열의 합 공식을 사용한 것이다
"""

def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer

