def dist(x1, x2):
    return (x1[0] - x2[0])**2 + (x1[1] - x2[1])**2

# 이론 블로그 참고
def solve(coords, N):
    # 점이 두 개일때는 두점 거리만 구하면 됩니다.
    if(N == 2):
        return dist(coords[0], coords[1])
    # 점이 세 개일때는 각 두점 사이의 거리를 구해서 최솟값을 구하면 됩니다.
    elif(N == 3):
        return min(dist(coords[0], coords[1]), dist(coords[1], coords[2]), dist(coords[0], coords[2]))
    
    mid = (coords[N//2][0] + coords[N//2-1][0]) // 2
    # x축을 기준으로 짧은 거리 d를 구합니다.
    d = min(solve(coords[:N//2], N//2), solve(coords[N//2:], N//2))
    
    # x 축 기준을 잊지 말것
    # 유효 거리 d보다 짧거나 같은 것을 제외하고 나머지는 제외시킵니다.
    # 즉, 두점 거리가 d보다 먼 경우는 제외합니다.
    short_check = []
    for subset in coords:
        if((mid - subset[0])**2 <= d):
            short_check.append(subset)
    short_check.sort(key = lambda x:x[1])
    
    if(len(short_check) == 1):
        return d
    else:
        y_check = d
        
        # x축만 고려하면 아직 고려해야할 점의 개수가 많이 남아있어 시간초과가 뜨게 됩니다.
        # 따라서 y축을 고려해주어 y축 기준의 d보다 긴 경우는 전부 제외시켜 주어야 합니다.
        # 세 가지 경우는 필수로 제외합니다.
        for i in range(len(short_check) - 1):
            for j in range(i+1, len(short_check)):
                # y축 기준, 기본적으로 최소 길이 d보다 사이 거리가 긴 경우 제외
                if(short_check[i][1] - short_check[j][1]) ** 2 > d:
                    break
                # 두 점 모두 왼쪽에 있는 경우
                elif(short_check[i][0] < mid and short_check[j][0] < mid):
                    continue
                # 두 점 모두 오른쪽에 있는 경우
                # 두 점이 mid를 지나는 점과 비교해보세요
                elif(short_check[i][0] > mid and short_check[j][0] > mid):
                    continue
                y_check = min(y_check, dist(short_check[i], short_check[j]))
                
    return y_check

import sys

# input = sys.stdin.readline
N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]

# 중복되는 점은 제거
# 블로그 참고
coords_set = list(set(map(tuple,coords)))
if len(coords_set) != len(coords):
    print("0")
else:
    coords_set.sort() # sorted(coords, key=lambda x:-x[0])
    print(solve(coords_set, N))