"""https://programmers.co.kr/learn/courses/30/lessons/72412"""


"""
사용한 논리 및 오류:
info와 query를 split()을 이용해 원소만 배열에 저장
반복문과 in을 사용해 포함이 되면 1추가
점수부분만 인덱스를 이용해 비교
*순서대로 query값을 배열에 저장하는점과 마지막 숫자 비교에서 수 많은 중첩을 낳기에
무언가 잘못되었다는것을 인지하였다
*하나의 쿼리당 전체 info를 반복해야하니 데이터의 지수만큼 시간이 걸리다
"""



def solution(info, query):
    count = []
    info_sp = []
    query_sp = []

    for i in info:
        info_sp.append(i.split(' '))
    
    for i in query:
        temp = i.split('and')
        query_sp.append(temp[:-2] + temp[-1].split(' '))
    
    for i in range(len(query_sp)):


    # for qry in query_sp[:-1]:
    #     for inf in info_sp:
    #         if int(qry) and int(inf):
    #             if int(qry) >= int(inf):
                    
