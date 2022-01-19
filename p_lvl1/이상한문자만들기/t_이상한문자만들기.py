"""https://programmers.co.kr/learn/courses/30/lessons/12930"""



"""
정답 변수와 임시 저장 변수 2개를 만들어서 공백이 있는 문자를 분리했다
다만 2개의 변수를 사용하느라 공간 효율성에서 떨어지는 코드를 작성할 수
밖에 없었다
"""



def solution(s):
    answer = ''
    test = ''
    count = 0

    for i in range(len(s)):
        if s[i]==" ":
            answer+= (test+" ")
            count = 0
            test=''
            continue

        if count%2==0:
            test+=s[i].upper()
            count+=1
        else:
            test+=s[i].lower()
            count+=1

        if (i+1)==len(s):
            answer+= test

    return answer
