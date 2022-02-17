"""https://programmers.co.kr/learn/courses/30/lessons/42578"""






from itertools import product

def solution(clothes):
    
    hash_table = {}

    for cloth in clothes:
        if cloth[1] in hash_table:
            hash_table[cloth[1]].append(cloth[0])
        else:
            hash_table[cloth[1]] = []
            hash_table[cloth[1]].append(cloth[0])


    value_list = hash_table.values()
    combination = list(product(*value_list))

    if len(hash_table.keys()) == 1:
        return len(combination)


    return len(combination) + sum([len(hash_table[x]) for x in hash_table])
