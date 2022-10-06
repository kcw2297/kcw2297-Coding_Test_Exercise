# d_stack 제거 개선
import sys
N = int(sys.stdin.readline().strip())
c_list = []
for _ in range(N):
    circle = list(map(int,sys.stdin.readline().strip().split()))
    # start,end, len으로 입력
    c_list.append([circle[0]-circle[1],circle[0]+circle[1],2*circle[1]])
# 시작점 순서대로 오름차순, 지름크기대로 내림차순 정렬
c_list.sort(key = lambda x : (x[0],-x[2]))
c_stack = []
ans = 1
for c in c_list:
    ans += 1
    cur_start,cur_end,cur_d = c
    if not c_stack: #최초 예외처리
        pass
    # 현재 원의 시작점과 끝점이 stack[-1] 원 안에 들어온다면 거리 수정
    elif cur_start >= c_stack[-1][0] and cur_end <= c_stack[-1][1]:
        c_stack[-1][2] -= cur_d
    # 안들어온다면 더큰원을 찾기위해 pop 하기
    else:
        while c_stack:
            if cur_start >= c_stack[-1][0] and cur_end <= c_stack[-1][1]:
                break
            temp = c_stack.pop()
            if temp[2] == 0:
                ans += 1
        if c_stack:
            c_stack[-1][2] -= cur_d
    # 현재원을 다음 조건으로 추가
    c_stack.append(c)
for c in c_stack:
    if c[2] == 0:
        ans += 1
print(ans)

#개선 1차
import sys
N = int(sys.stdin.readline().strip())
c_list = []
for _ in range(N):
    circle = list(map(int,sys.stdin.readline().strip().split()))
    # start,end, len으로 입력
    c_list.append((circle[0]-circle[1],circle[0]+circle[1],2*circle[1]))
# 시작점 순서대로 오름차순, 지름크기대로 내림차순 정렬
c_list.sort(key = lambda x : (x[0],-x[2]))
c_stack = []
d_stack = []
ans = 1
for c in c_list:
    ans += 1
    cur_start,cur_end,cur_d = c
    if not c_stack: #최초 예외처리
        pass
    # 현재 원의 시작점과 끝점이 stack[-1] 원 안에 들어온다면 거리 수정
    elif cur_start >= c_stack[-1][0] and cur_end <= c_stack[-1][1]:
        d_stack[-1] -= cur_d
    # 안들어온다면 더큰원을 찾기위해 pop 하기
    else:
        while c_stack:
            if cur_start >= c_stack[-1][0] and cur_end <= c_stack[-1][1]:
                break
            c_stack.pop()
            if d_stack.pop() == 0:
                ans += 1
        if d_stack:
            d_stack[-1] -= cur_d
    # 현재원을 다음 조건으로 추가
    c_stack.append(c)
    d_stack.append(cur_d)
for d in d_stack:
    if d == 0:
        ans += 1
print(ans)


#개선전
# import sys
# N = int(sys.stdin.readline().strip())
# c_list = []
# for _ in range(N):
#     circle = list(map(int,sys.stdin.readline().strip().split()))
#     # start,end, len으로 입력
#     c_list.append((circle[0]-circle[1],circle[0]+circle[1],2*circle[1]))
# c_list.sort(key = lambda x : (x[0],-x[2]))
# c_stack = []
# d_stack = []
# ans = 1
# for c in c_list:
#     if not c_stack:
#         c_stack.append(c)
#         d_stack.append(c[2])
#         ans += 1
#         continue
#     cur_start,cur_end,cur_d = c
#     past_start,past_end = c_stack[-1][0],c_stack[-1][1]
#     if cur_start >= past_start and cur_end <= past_end:
#         ans += 1
#         d_stack[-1] -= cur_d
#         c_stack.append(c)
#         d_stack.append(cur_d)
#     else:
#         while c_stack:
#             if cur_start >= c_stack[-1][0] and cur_end <= c_stack[-1][1]:
#                 break
#             c_stack.pop()
#             if d_stack.pop() == 0:
#                 ans += 1
#         ans += 1
#         if d_stack:
#             d_stack[-1] -= cur_d
#         c_stack.append(c)
#         d_stack.append(cur_d)
# for d in d_stack:
#     if d == 0:
#         ans += 1
# print(ans)



# import sys

# N = int(sys.stdin.readline())
# points = []
# for _ in range(N):
#     x, r = list(map(int, sys.stdin.readline().split()))
#     # x 원의 중심 좌표, r: 원의 반지름

#     points.append(["{", x-r, 0, 0])
#     # 1: 원의 왼쪽을 표시하는 괄호
#     # 2: 원의 왼쪽 좌표 x-r
#     # 3: 상태(이어지면 1, 아니면 0)
#     # 4: 이어진 원 지름 길이의 합
#     points.append([")", x+r, 0, 0])  # 원의 오른쪽

# points.sort(key=lambda x: (x[1], x[0]))

# stack = []
# answer = 1  # 영역개수, 무조건 제일 바깥 영역 하나는 있기에 1부터 시작

# for i in range(len(points)):  # 원의 좌표를 왼쪽부터 차례로 탐색

#     if points[i][0] == "{":  # i번째 좌표가 원의 왼쪽이라면

#         if stack:  # 만약 stack에 element가 있다면/ stack element는 point와 동일한 형태

#             if stack[-1][1] == points[i][1] or stack[-1][3] == points[i][1]:
#                 # 1: stack의 제일 뒤 element의 좌표가 현재 i번째 좌표와 같거나,
#                 # 2: stack좌표부터 이어지고 있는 길이가 현재 좌표와 같다면(이전 원과 지금 원이 이어지고 있다면)

#                 stack[-1][2] = 1  # 이전 원의 좌표는 이어지고 있다고 상태를 기록
#             else:
#                 stack[-1][2] = 0  # 그렇지 않을 경우 안이어지고 있다고 상태를 기록

#         stack.append(points[i])

#     else:  # i번째가 원의 오른쪽이라면,
#         half = stack.pop()  # stack의 제일 뒤 element를 pop

#         if stack and stack[-1][2] == 1:  # stack에 element가 있고, 그것이 이어지고 있다고 되어있다면
#             stack[-1][3] = points[i][1]
#             # stack 이어진 원지름의 길이의 합을 현재 element의 좌표로 업데이트

#         if half[2] == 1 and half[3] == points[i][1]:
#             answer += 1  # 현재의 경우 원이 충분히 이어져서 위 아래로 영역이 나뉘었기에 답에 1을 추가해준다.

#         answer += 1  # 그리고 원이 닫히면서 하나 기본적인거 추가.

# print(answer)
