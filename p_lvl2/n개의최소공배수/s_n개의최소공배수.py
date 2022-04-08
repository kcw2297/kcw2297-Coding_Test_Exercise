




"""
최소공배수 = (x*y)//gcd(x,y) == 최소공배수와 최대공약수 사이의 관계 활용
최소공배수를 answer에 저장하면서 새로운 값과 비교
"""





def solution(arr):
    from math import gcd                           
    answer = arr[0]                                 

    for num in arr:
        answer = answer*num // gcd(answer, num)     

    return answer