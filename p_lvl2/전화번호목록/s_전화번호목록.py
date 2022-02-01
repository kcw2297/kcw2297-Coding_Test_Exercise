



"""
해시를 사용하는 이유는 시간 복잡도가 O(1)이라는 큰 장점이 있다
하지만 밑에 코드는 for를 2번 중첩하여 사용하였기에 O(n*n)이 아닌가싶다

해시는 key-value 형태로 특정한 값을 빠르게 찾는데 좋은 알고리즘으로
이번 문제처럼 특정 키가 다른 키에 포함되는지 확인할 때 사용한다

jubdoo가 해시맵에 있고 phone_number가 아닌 경우를 쓴 이유는, 접두사는
hash_map에 있지만 비교대상이 아니기 때문이다
"""




def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True



"""
다른 문제 풀이로 startswith를 사용한 예시이다
접두사를
"""

    def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1)
        print(p2)
        if p2.startswith(p1):
            return False
    return True
