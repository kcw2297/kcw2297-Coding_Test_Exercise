


"""
set와 좌표 x,y를 활용해 풀어냈다
set에 저장시 일정한 규칙을 정하면 별다른 조건없이
동일한 값을 처리할 수 있다.
"""

def solution(dirs):
    visit = set()
    x =  y = 0
    for d in dirs:
        if d == 'U' and y < 5:
            visit.add(((x, y), (x, y+1)))
            y += 1
            
        elif d == 'D' and y > -5:
            visit.add(((x, y-1), (x, y)))
            y -= 1
            
        elif d == 'R' and x < 5:
            visit.add(((x, y), (x+1, y)))
            x += 1
            
        elif d == 'L' and x > -5:
            visit.add(((x-1, y), (x, y)))
            x -= 1
    return len(visit)



"""
사용한 논리:
집합을 이용한 풀이로 좌표 x,y를 따로 분리해서 계산하는 것이 편리한 것으로 보인다
"""

def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
