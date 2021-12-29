"""
완전탐색 문제로 가장 효율성이 않좋은 for loop을 중첩으로 사용한 brute loop방식이다
"""

"""
배운점 :
비교 대상이 있고 각 대상이 갖는 요소의 숫자가 다를 경우
dictionary로 저장하여 해당 값을 하나씩 저장한다

인덱스 값 설정을 보통 len() %로 구할 수 있다
"""

def solution(answers):
    student = {1:[1,2,3,4,5], 2:[2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5]}
    score = {1:0, 2:0, 3:0}
    for idx, answer in enumerate(answers):
        for key, value in student.items():
            if answer == value[idx % len(value)]:
                score[key] += 1
    highest = max(score.values())
    result = [key for key, value in score.items() if value == highest]

    return result
