"""https://programmers.co.kr/learn/courses/30/lessons/17677"""



"""
틀린 접근 :
문제에서 문자 이외의 것은 다중집합 원소로 만들지 않는다는 대목에서 헷갈렸다
나는 처음 시작시 문자열만 남긴 후에 집합을 만들었는데, 이는 추가 원소를 만들었다
"""

"""
내가 사용한 논리 :
    자카드 => 2개의 집합을 교집합/합집합 한 것
    다중 집합의 교집합은 min/max를 이용 x
    
    문자열은 2문자씩 끊어서 다중집합을 만듬 x
    
    전부 소문자화하고, 오직 문자만 계산한다 x
    
    마지막에 65536를 곱한 후에 소수점을 버린다 x
"""
    


def solution(str1, str2):  
    low1, low2 = str1.lower(), str2.lower()

    low1 = checkStr(low1)
    low2 = checkStr(low2)

    low1 = divide(low1)
    low2 = divide(low2)

    diff_ = set(low1) & set(low2)
    union_ = set(low1) | set(low2)

    diff = []
    for i in diff_:
        for _ in range(min(low1.count(i), low2.count(i))):
            diff.append(i)
    
    union = []
    for i in union_:
        for _ in range(max(low1.count(i), low2.count(i))):
            union.append(i)
    
    jcard = len(diff)/len(union)
    return int(65536 * jcard)


def checkStr(str):
    new_str = ""
    for el in str:
        num = ord(el)
        if num<97 or num > 122:
            continue
        else:
            new_str += el
    return new_str

def divide(str):
    container = []
    for i in range(1,len(str)):
        container.append(str[i-1:i+1])
    return container