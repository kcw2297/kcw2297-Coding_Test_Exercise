"""https://programmers.co.kr/learn/courses/30/lessons/68644"""

"""
set를 이용하여 중복되는 값을 제거하고 for loop으로 처음부터 전체를
더하가면서 값을 찾으려고 했다.
for loop를 2번 중첩함으로써 시간 효율성도 떨어지고 코드가 생각보다 더럽
"""

"""
수학적 사고 능력이 알고리즘에서 중요하다는 것을 깨달았다
for loop만 쓰는 것에 한계를 많이 느끼고 순열,조합 등등
개념을 다시 볼 필요를 느낀다
"""

def solution(numbers):
    answer = set()
    for x in range(len(numbers)):
        for y in range(x+1,len(numbers)):
            result = numbers[x] + numbers[y]
            answer.add(result)
    answer = list(answer)
    answer.sort()
    return answer
