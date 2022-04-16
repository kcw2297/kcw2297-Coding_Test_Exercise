


"""
사용한 논리:
이진탐색에서는 시작점과 끝점 및 중간점을 이용해 logn의 시간효율성을 가진다
"""



def bin_search(start:int, end: int, lst:list,target_value:int):
    # start == end 인 경우에도 정답이 될 수 있다. --> 딱 중간에서 만났을때
    if start > end:
        return 0

    else:
        mid = (start+end)//2
        mid_value = lst[mid]
        if mid_value == target_value:
            return 1
        # 재귀로 돌리면 이미 검사한 mid는(idx)는 검사 범위에 안들어가게 해야한다
        # return 값을 재귀의 결과로 받아야한다. 함수가 스택에서 빠져나가면서 위로 return 결과를 들고 오기 때문.
        # 그렇지 않다면 그대로 검색 결과가 그대로 증발한다.
        elif mid_value > target_value:
            return bin_search(start,mid-1,lst,target_value)
        elif mid_value < target_value:
            return bin_search(mid+1,end,lst,target_value)


N = int(input())
num_lst = list(map(int,input().split()))
M = int(input())
target_num_lst = list(map(int,input().split()))

num_lst.sort()

for num in target_num_lst:
    print(bin_search(0,N-1,num_lst,num))

