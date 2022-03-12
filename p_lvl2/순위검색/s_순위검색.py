
"""
사용한 논리:
조합과 이분탐색 및 3가지 라이브러리
brute force를 하기에는 데이터의 양의 지수적으로 시간이 걸리기에, 이분탐색을 하여 log(n)이 걸린다
defaultdict를 활용하여 주어지는 key에 리스트 배열을 넣고, 배열 안에 점수를 넣는다
주어진 info를 조합으로 만든 후 해당 값을 key 그리고 score를 value로 넣는다

queries의 score부분은 bisect_left에서 이분탐색 시 사용된다
"""




from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]  # [java,	backend, junior, pizza]
        score = int(info[-1]) # 150
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-" # ['','-','','-','']
                key = ''.join(tmp) # "javapizza-senior"
                dic[key].append(score) 

    # 동일한 key인 경우, score를 기준으로 정렬
    for value in dic.values():
        value.sort()   

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])   
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)      
    return answer
