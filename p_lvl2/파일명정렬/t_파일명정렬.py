"""
https://programmers.co.kr/learn/courses/30/lessons/17686
"""



"""
사용한 논리 및 오류:
각 입력을 소문자로 바꾼다
head와 number를 따로 저장한다
다중 정렬을 한다
이후 분리된 문자를 합친다

* 소문자로 변환후 계산을 하였지만, 반환은 다시 대문자로 해야한다
* list slice를 이용해 분리하려고 하였지만 에러 발생
"""

def separate_str(list):
    end = 0
    for ele in list:
        try:
            int(ele)
            break
        except:
            end += 1
    return end

def separate_num(list):
    end = 0
    for ele in list:
        try:
            int(ele)
            end += 1
        except:
            break
    return end


def solution(files):
    temp = []
    lists = []
    answer = []

    #소문자로 변환한다
    for file in files:
        temp.append(file.lower())

    # head, number, tail로 분리한다
    for l in temp:
        end = separate_str(l)
        head = l[0:end]
        e = separate_num(l[end-1:])
        number = l[end-1:e]
        tail = l[e-1:]
        lists.append([head,number,tail])
    
    # 다중정렬한다
    sorting = sorted(lists, key = lambda x: (x[0], x[1]))

    for ele in sorting:
        answer.append(''.join(ele))

    return answer