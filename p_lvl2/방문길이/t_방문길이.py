"""https://programmers.co.kr/learn/courses/30/lessons/49994"""


"""
사용한 논리 및 오류:
현재 좌표평면을 지속적으로 기록한다

좌표평면을 이동시키고 리스트 변수에 저장한다
만약 새로 추가하는 경우에는 1을 더하고 아니면 1을 더하지 않는다

이동키 문자에 따라 현재 좌표에서 이동 여부를 바꾼다
예외 케이스로 좌표평면이 한계를 벗어날시 무시한다

오류 :
데이터 타입을 LIST로 잡아서 진행하였다. 그 이유로 순서가 있으며 index참고가
쉬워서 사용하였다. 하지만 이번 케이스에서는 set()를 활용하는게 맞았다.
동일한 여부를 체크하는 문제에서는 set만큼 효율적인 데이터 타입이 없다는 것을
간과하였다. 
"""

def check(cur, alpha ,mov):
    if cur+alpha in mov:
        return False
    else:
        return True


def solution(dirs):
    dirs = list(dirs)
    count = 0
    cur = [0,0]
    movements = []

    for dir in dirs:
        if dir == 'U':
            if (cur[1] + 1) <= 5 and check(cur, ['U'] ,movements):
                movements.append(cur+['U'])
                temp = cur[:]
                temp[1]+=1
                movements.append(temp+['D'])
                count += 1
            cur[1] += 1

        elif dir == 'D':
            if (cur[1] - 1) >= -5 and check(cur,['D'] ,movements):
                movements.append(cur+['D'])
                temp = cur[:]
                temp[1]-=1
                movements.append(temp+['U'])
                count += 1
            cur[1] -= 1
        elif dir == 'R':
            if (cur[0] + 1) <= 5 and check(cur, ['R'] ,movements):
                movements.append(cur+['R'])
                temp = cur[:]
                temp[0]+=1
                movements.append(temp+['L'])
                count += 1
            cur[0] += 1
        elif dir == 'L':
            if (cur[0] - 1) >= -5 and check(cur, ['L'] ,movements):
                movements.append(cur+['L'])
                temp = cur[:]
                temp[0]-=1
                movements.append(temp+['R'])
                count += 1
            cur[0] -= 1

    return count

