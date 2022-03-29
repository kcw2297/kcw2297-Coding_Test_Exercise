




"""
사용한 논리:
list()안에 문자열을 넣어 각 문자를 리스트안에 원소들로 저장
for 문을 사용하여 skill에 포함 될 시 pop(0)으로 앞에 꺼부터 제거
for else를 사용하여 if문의 조건에서 break가 아닌경우 1을 더한다
"""




def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer