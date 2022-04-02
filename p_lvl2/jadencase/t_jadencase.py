"""https://programmers.co.kr/learn/courses/30/lessons/12951"""




"""
사용한 논리:
공백으로 분리한 후에 capitalize하고 다시 공백으로 추가

"3people unFollowed me"	"3people Unfollowed Me"
"""



def solution(s):
    div = s.split(' ')
    answer = []
    for ele in div:
        answer.append(ele.capitalize())
    
    return " ".join(answer)
