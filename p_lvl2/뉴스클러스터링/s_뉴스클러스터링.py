

"""
사용한 논리 :
1. 전체 문자를 소문자로 바꾼다
2. isalpha()함수를 사용하여 알파벳인지 확인한다
3. 문자열에서 알파벳인 경우에만 두 문자열로 저장한다
4. Counter()의 고유 매소드인 elements()는 결과를 Counter object가 아닌 리스트로 반환
5. 2개의 Counter object를 &와 |를 이용해 교집합, 합집합을 구한다
"""





from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
            
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)