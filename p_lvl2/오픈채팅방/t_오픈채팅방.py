"""https://programmers.co.kr/learn/courses/30/lessons/42888"""



"""
문제에서 얻은 힌트는 다음과 같다 :
-가장 마지막에 있는 요소의 닉네임이 최종 닉네임이다
-id는 고유번호이기에 변경이 안된다
이를 이용해서 for loop으로 가장 마지막에 있는 값과 id를 dict형태로 저장한다
"""



    for record in records:
        record = record.split()
        if len(record)==3:
            last_name[record[1]] = record[2]

    for record in records:
        record = record.split()
        if record[0] == 'Enter':
            answer.append(f'{last_name[record[1]]}님이 들어왔습니다.')
        elif record[0] == 'Leave':
            answer.append(f'{last_name[record[1]]}님이 나갔습니다.')
    return answer





"""
처음 문제 접근을 리스트에 아이디와 닉네임을 튜플 형식으로 저장한후에
change나 re-enter가 나올시에 전부 바꾸는 형식으로 하려했다. 하지만
string으로 저장된 상태에서 닉네임만 변경하는데 어려워서 접었다
"""

"""
def solution(records):
    answer = []
    for record in records:
        if check(record):
            answer.append((check(record),record[1]))
        else:


def check(record):
    if record[0] =="Enter":
        return f'{record[2]}님이 들어왔습니다.'
    elif record[0] =="Leave":
        return f'{record[2]}님이 나갔습니다.'
    else:
        return 0
"""
