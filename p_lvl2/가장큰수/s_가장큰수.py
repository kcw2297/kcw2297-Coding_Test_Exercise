
"""
1.문제에서 문자열로 반환을 하라고 하였기에 map(str,배열)로 전환한다
2.sort()를 이용해서 순서를 바꾸는데, 문자열에 3을 곱해 1~1000의
자리수까지 비교한다
3. int()로 하여서 "000"을 0으로 바꿔준다
"""


def solution(num):
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(num)))


"""
functools중에 cmp_to_key(함수)를 이용해서 푼 풀이이다

"""



import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
