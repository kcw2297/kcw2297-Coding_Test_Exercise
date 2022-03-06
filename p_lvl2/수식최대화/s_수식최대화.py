


"""
정답 논리:
    분할 정복과 재귀함수를 이용해 풀어낸 문제이다
    연산자를 기준으로 분할을 한다
    피연산자만 남는 경우 반환을 하여 재귀함수에 있는 계산을 한다
    최종적으로 가장 큰 수를 반환한다
    *연산자가 3가지 밖에 없으니 3!의 경우의 수가 있어 이를 반복한다
"""


from itertools import permutations


def calc(op, seq, exp):
    if exp.isdigit():  # 더이상 exp에 연산자가 없으면
        return str(exp)  # 그대로 리턴
    else:  # 현 순위 연산자에 따라 진행
        if op[seq] == "*":
            split_data = exp.split("*")  # 연산자로 쪼갬
            temp = []
            for s in split_data:  # 쪼개진 각 부분에 대해 재귀
                temp.append(calc(op, seq + 1, s))
            return str(eval("*".join(temp)))  # 재귀 실행 결과를 담은 배열에 대해 eval()함수로 계산

        if op[seq] == "+":
            split_data = exp.split("+")
            temp = []
            for s in split_data:
                temp.append(calc(op, seq + 1, s))
            return str(eval("+".join(temp)))

        if op[seq] == "-":
            split_data = exp.split("-")
            temp = []
            for s in split_data:
                temp.append(calc(op, seq + 1, s))
            return str(eval("-".join(temp)))

def solution(expression):
    answer = 0
    # 6가지 operation 정의
    operations = list(permutations(['*', '+', '-'], 3))

    for op in operations:  # 정의된 op에 따라 calc 재귀 진행
        result = abs(int(calc(op, 0, expression)))  # 얻어낸 결과값에 대해 절대값 취함.

        if result > answer:  # 기존의 결과값과 비교
            answer = result

    return answer   


"""
다른 이의 풀이로, 3!의 경우의 수 만큼 반복했다
split이후에 list comprehension + f'({i})'를 이용해 괄호를 넣었다
이런식으로 마지막에 남은 연산자가 첫번째고, 처음 나눈 연산자가 마지막이된다
끝으로 abs()와 eval()로 계산한후 max()로 가장 큰 값을 구한다
"""



def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)