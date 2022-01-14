



"""
2개의 dict을 이용하여 확인하는거 까지는 맞았지만 이후에 숫자로 변환하는
과정을 for loop을 2번 이용하여 전환한다
"""

"""
특정 값에만 해당되는 값들을 저장시에 dict 안에 list를 value를 넣어서
구분하고 이후에 index를 이용해 확인한다
"""


def solution(id_list, report, k):
    answer = []
    a = list(set(report))
    dictionary2 = {name : 0 for name in id_list}
    dictionary = {name : [] for name in id_list}
    for i in a:
        dictionary[i.split()[1]].append(i.split()[0])

    for i in dictionary:
        if len(dictionary[i]) >= k:
            for j in dictionary[i]:
                dictionary2[j] += 1

    for i in dictionary2:
        answer.append(dictionary2[i])

    return answer
