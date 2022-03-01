



from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    max_values = []
    menus = []

    for c in course:
        menu = []
        for order in orders:
            menu_candidate = combinations(sorted(order),c)
            #	[('X', 'Y'), ('X', 'Z'), ('Y', 'Z'), ('W', 'X'), ('W', 'Y'), ('X', 'Y'), ('A', 'W'), ('A', 'X'), ('W', 'X')]
            menu += [a for a in list(menu_candidate)]
            

        if len(menu) >= 1:
            max_values.append(Counter(menu).most_common(1)[0][1])
            menus.append(menu)
    
    for max_, menu in zip(max_values, menus):
        for key, values in Counter(menu).items():
            #	Counter({('X', 'Y'): 2, ('W', 'X'): 2, ('X', 'Z'): 1, ('Y', 'Z'): 1, ('W', 'Y'): 1, ('A', 'W'): 1, ('A', 'X'): 1})
            if max_ == values and values >= 2:
                answer.append("".join(key))
    return sorted(answer)



