




"""
총 인용된 횟수는 for loop를 통해 1개씩 증가하면서 각 논문과 비교한다
논문 배열은 정렬을 해논 상태이기 때문에 인덱스 마이너스로 뒤에서 부터
값을 가져온다
"""





def solution(citations):
    answer = 0
    citations.sort()

    for i in range(1, len(citations)+1):
        min_num = citations[-i]
        if min_num >= i:
            answer = i

    return answer
