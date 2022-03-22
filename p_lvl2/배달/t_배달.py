"""https://programmers.co.kr/learn/courses/30/lessons/12978"""



"""
사용한 논리 및 오류:
각 노드를 기준으로 다음 노드로의 거리를 dict과 list로 저장한다
재귀함수를 이용해서, 다음 노드로 이동하고 값을 저장한다
*재귀함수를 사용하려면 재귀의 마지막 부분부터 반환을 하여야하지만
이를 구현하기가 쉽지 않았다
"""


def solution(N, road, K):
    n_road = {}

    #노드별 이동거리를 정리
    for dist in road:
        try:
            n_road[dist[0]]
        except:
            n_road[dist[0]] = []

        n_road[dist[0]].append({dist[1]:dist[2]}) #{1:[{2:3},{4:1}]}
    
