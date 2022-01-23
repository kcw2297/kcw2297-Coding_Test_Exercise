"""https://programmers.co.kr/learn/courses/30/lessons/12950"""







def solution(arr1, arr2):
    answer = []
    mom = []
    for i in range(len(arr1)):
        a = arr1[i]
        b = arr2[i]

        for j in range(len(a)):
            good = a[j]+b[j]
            mom.append(good)
        answer.append(mom)
        mom=[]
    return answer
