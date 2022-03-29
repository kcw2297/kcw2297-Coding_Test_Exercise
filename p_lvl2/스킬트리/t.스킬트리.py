"""https://programmers.co.kr/learn/courses/30/lessons/49993"""




"""
사용한 논리:
skill_trees의 값 중 skill에 해당하는 것 외에는 전부 지운다
이후 남은 문자와 skill을 순서대로 비교하여 다 맞으면 1을 더한다
"""

def shrink(tree, skill):
    text = ""
    for ele in tree:
        if ele in skill:
            text += ele
    return text

def check(text, skill):
    for idx in range(len(text)):
        if text[idx] != skill[idx]:
            return False
    return True


def solution(skill, skill_trees):
    count = 0

    for tree in skill_trees:
        text = shrink(tree, skill)
        if check(text, skill):
            count += 1
    
    return count


