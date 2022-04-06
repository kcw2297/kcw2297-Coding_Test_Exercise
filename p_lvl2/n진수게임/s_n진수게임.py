

"""
사용한 논리:
10진수에서 n진수로 변환하는 방법과 순서를 반복하는 것을 구현해야하는 문제였다
n진수 변환 문제같은 경우는 주어진 십진수에서 n진수를 나누고 나머지 값을 더한다
"""

def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        # q를 base로 변환
        # 즉, n진수의 다음 자리를 구함
        return convert(q, base) + temp[r]
    
def solution(n, t, m, p):
    answer = ''
    test = ''
    
    for i in range(m*t):
        test += str(convert(i, n))
        
    while len(answer) < t:
        answer += test[p-1]
        p += m
        
    return answer





"""
divmod대신에 %와 //으로 직접 나머지와 몫을 구한다
개선사항 : temp = '' 로 변경하고 temp = data[number%n] + temp로 
변경하면 밑에서 리버스하여 조인을 할 필요 없어집니다
"""


def solution(n, t, m, p):
    data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    numbers = "0"
    for number in range(1, t*m):
        temp = ''
        while number > 0:
            temp = data[number%n] + temp
            number //= n
        numbers += "".join(temp)

    return numbers[p-1:t*m:m]

