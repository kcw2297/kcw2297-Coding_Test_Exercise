




"""
n-1로 잡은 이유는 3진법에는 0이 포함되어 있지 않기에 정수 n은 1이 더 큰거다

recursion을 이용해서 3으로 나눌 때마다 몫은 자리수를 넓히는데 사용된다
"""

div solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q,r = divmod(n-1,3)
        return solution(q)+'124'[r]
