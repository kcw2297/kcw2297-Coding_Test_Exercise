"""https://programmers.co.kr/learn/courses/30/lessons/81302"""


"""
bfs를 이용해 풀어낸 문제로 deque()를 정의하여 방문 노드를 체크하면서 다음
노드와 비교한다

배운점 :
deque()안에는 iterable한 객체만 인자로 받는다 :
deque()에허 iterable하지 않는 요소를 넣을경우 에러가 난다
ex) [1,2]는 에러가 나오니 [[1,2]]로 list형식으로 만들어 넣어야한다

pop()이후 받는 변수의 개수에 따라 데이터 형식이 다르게 나온다
ex) a=[[1,2]]인 경우, x,y = a.pop()할시에는 1,2로 나누어 나온다

visited와 distance로 2개의 table을 만들어 각 노드별 경로를 확인한다
"""


"""
https://www.youtube.com/watch?v=hCVgKE6qwFs
"""
