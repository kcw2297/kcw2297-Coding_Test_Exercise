




"""
pop과 append로 접근하는 것보다 deque로 접근하는 것이 더 빠르다
deque를 사용하기 위해 deque()로 호출한후 변수에 저장한다
deque를 사용하는 경우는 보통 pop()을 사용하기에 while이나 특정 조건에
deque()에 요소가 있냐 없냐고 설정한다


리스트 안에 요소와 index를 함께 관리가 필요한 경우 enumerate()을 활용하여 tuple로
리스트 안에 저장한다
"""




from collections import deque

def solution(priorities, location):
  answer = 0

  d = deque([(v,i) for i,v in enumerate(priorities)])

  while len(d):
      item = d.popleft()
      if d and max(d)[0] > item[0]:
          d.append(item)
      else:
          answer += 1
          if item[1] == location:
              break
  return answer
