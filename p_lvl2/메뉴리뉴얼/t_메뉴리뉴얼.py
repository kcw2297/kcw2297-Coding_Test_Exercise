"""https://programmers.co.kr/learn/courses/30/lessons/72411"""



"""
문제 설명이 길어서 읽는데만해도 시간 소요가 컸다.
조합을 묻는 질문에 바로 떠올려야하는 것이 combinations과 Counter이다
전체 조합 중 가장 많은 것을 고르는 것으로 most_common method를 사용한다
"""

"""
사용한 논리 :
각 코스별 주문의 조합 중에서 가장 많은 것을 반환하는 것임으로
코스별로 반복문을 돌리고 주문별로 반복문을 돌린다

**
combinations()가 반환하는 것은 배열이 아닌 objects로 반환되기 때문에
리스트로 사용하기 위해서는 list()로 변환하여야한다

순서 :
1. 코스별로 반복을 하기 위해 course를 for loop한다
2. 코스별 메뉴를 배열에 저장하기 위해 배열 변수를 설정한다

3. 주문별로 for loop을 한다
4. combinations(배열,코스)로 주문의 조합을 갖는다
5. 각 조합(투플로되어있다)을 메뉴 배열에 저장한다

6. Counter와 most_common을 사용하여서 가장 value가 높은 값을 변수에 저장한다
7. 메뉴들은 menus 배열 변수에 저장

8. 위의 loop를 마친후에 zip과 items()를 이용해 key-value를 비교해 최종 정답에 저장한다
"""


