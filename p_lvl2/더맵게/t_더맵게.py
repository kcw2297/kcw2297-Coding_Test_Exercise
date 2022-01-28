"""https://programmers.co.kr/learn/courses/30/lessons/42626"""



"""
heappop과 heappush를 할 때마다 tree를 정렬하기에 시간이 많이 걸릴것으로 예상한다
try와 except을 활용해서 에러가 나올 때 -1을 반환하기로 했다. 하지만 이는 에러가
나올 때까지 불필요한 looping을 하기에 비효율적이다
"""

"""
시간 효율성 : O(nlogn)
공간 효율성 : O(1)
"""


import heapq

def solution(scoville, K):

    count = 0
    heapq.heapify(scoville)

    while scoville[0]<K:
        try:
            sm = heapq.heappop(scoville)
            md = heapq.heappop(scoville)
            lg = sm+(md*2)
            heapq.heappush(scoville,lg)
            count+=1
        except:
            return -1

    return count
