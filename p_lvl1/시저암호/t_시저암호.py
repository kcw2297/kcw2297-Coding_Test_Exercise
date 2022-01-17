"""https://programmers.co.kr/learn/courses/30/lessons/12926"""



"""
ord와 chr를 활용해서 값을 구하려 하였지만 공백 및 알 수 없는 부분에서
실패가 나왔다
"""

"""
list(str)을 활용하여서 문자열에 있는 공백을 추후 고려하지 않아도 된다
"""



def solution(s, n):

    answer = ""
    for ele in range(len(s)):
        word = s[ele]
        asc = ord(word)

        if word==" ":
            answer+=word
            continue


        if word.islower():
            if asc+n>122:
                over=asc+n-122
                new_ele = chr(over+96)
                answer+=new_ele
                continue
            answer+= chr(asc+n)

        elif word.isupper():
            if asc+n>91:
                over=asc+n-91
                new_ele = chr(over+64)
                answer+=new_ele
                continue
            answer+= chr(asc+n)
    return answer
