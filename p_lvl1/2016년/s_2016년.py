"""
머리속에 잠시 생각했지만 시도를 안해본 코드인데,
결과적으로 이 접근 방식이 더 간결하고 쉬웠다
"""

"""
각 월별로 시작하는 요일이 다르기에, 전체에서 7을 나누는 것이다
"""


def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
