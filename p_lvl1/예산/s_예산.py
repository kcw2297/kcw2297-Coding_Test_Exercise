

"""
pop()을 사용하여서 뒤에서 부터 조건에 부합하지 않는 값을 뺐다
이로인해 새로운 메모리를 사용하지 않고 문제를 풀었다
"""



def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
