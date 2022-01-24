"""https://programmers.co.kr/learn/courses/30/lessons/12940"""



"""
주어진 예제에만 맞게하고 문제의 본질은 풀지 못하였다
최대 공약수는 전체 약수에서 set의 교집합으로 구하였지만
최소공배수에서 막혔다
"""


def solution(n, m):
    answer = []

    n_num = [ele for ele in range(1,n+1) if n%ele==0]
    m_num = [ele for ele in range(1,n+1) if m%ele==0]

    same = set(n_num)&set(m_num)
    answer.append(max(same))

    if max(same) ==1:
        answer.append(n*m)
    else:
        if n>m:
            answer.append(n)
        else:
            answer.append(m)
