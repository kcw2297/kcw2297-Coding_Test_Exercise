



"""
사용한 논리:
sorted를 이용해 key=len를 활용 => legnth를 기준으로 정렬한다는 것이다
다시 s.split(',')를 하여서 저장되는 원소들이 배열로 묶어진다
이후 result배열 변수에 하나식 저장한다
"""

"""
배운점:
이 문제에서 가장 걸림돌은 {,}으로 이를 구분하는 split함수를 
사용하는 것과, 순서대로 값을 저장하여야하니 sorted(key=len)를 사용한다
"""


def solution(s):
    ls = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)
    result = []
    for l in ls:
        for s in l:
            if int(s) not in result:
                result.append(int(s))
                break
    return result


"{{2},{2,1},{2,1,3},{2,1,3,4}}"

def solution(s):
    s = eval(s.replace("{", "[").replace("}", "]"))
    answer = list({num:0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
    return answer


"""
다른 풀이로 문자 {}를 []로 바꾸어 풀어준 모습이다
그다음 eval()를 이용해 문자열을 배열로 바꾸었다
"""

def solution(s):
    s = eval(s.replace("{", "[").replace("}", "]"))
    for k in sorted(s, key=lambda x: len(x)):
        for num in k:
            answer = list({num:0}.keys())
    return answer