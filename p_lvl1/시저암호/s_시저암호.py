


"""
문자열의 list()로 변환시 띄어쓰기도 list의 한 element로 저장된다
이를 이용해서 중간에 공백을 고려하지 않게 되었다
"""




def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
