


"""
10 때문에 계산하는데 복잡함이 있었기에 replace와 if문을 이용하여서
list 형식으로 단위를 나누었다
"""

"""
데이터 형식을 dict이 아닌 list를 활용하여 idx으로 풀어간 모습이다.
거의 대부분 코딩테스트에서 list comprehension과 idx를 짝꿍으로 묶어가는게 맞아 보인다
"""

def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
