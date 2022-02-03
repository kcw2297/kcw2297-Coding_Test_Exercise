




"""
가장 작은 수에서 가장 큰 수를 곱해야 전체 값이 최소가 된다
이를 이용해 sort()와 sort(reverse=True)로 정렬한후 곱한다
"""



def solution(a,b):
    a.sort()
    b.sort(reverse=True)

    return sum([c*d for c,d in zip(a,b)])
