







"""
사용한 논리:
공백을 기준으로 분리한 후에 capitalize를 하고 다시 배열에 저장한다
이후 join함수로 붙인다
"""




def solution(s):
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:]) 
    return " ".join(answer)