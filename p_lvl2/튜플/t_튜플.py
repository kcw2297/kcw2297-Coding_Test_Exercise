"""https://programmers.co.kr/learn/courses/30/lessons/64065"""

"""
사용한 논리 및 오류:
가장 큰 set를 찾는다 
해당 길이에서 -1로 loop을 돌린다
해당 set와 그다음 set의 빼서 남는 값을 저장
마지막에 reverse
*주어진 값이 set가 아닌 string이었다..
"""


def solution(s):
    answer = []

    for i in s:
        if len(s) == len(i):
            start = i
            break
    
    for j in range(len(s)-1, 0, -1):
        for y in s:
            if j == len(y):
                diff = sum(start) - sum(y)
                answer.append(diff)

    return answer.reverse()
    


"""
사용한 논리 및 오류:
주어진 s를 처음부터 반복을하여 1~len(s)까지 차례로 answer변수에 저장하려했다
문제는 처음 값을 저장시에 설정하는게 어렵고 4중 중첩 loop으로 오류가 많다
"""

def solution(s):
    answer = []
    #1부터 시작하여 길이가 1인 set부터 len(s)길이인 set까지 확인
    for i in range(1,len(s)+1):
        for j in s:
            if len(j) == i:
                #해당 길이인 set 내에 원소를 answer 변수에 저장
                for x in answer:
                    for ele in j:
                        if y not in x:
                            answer.append(y)
    return answer