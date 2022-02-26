


"aabbaccc"	7 => 2a2ba3c

def solution(s):
    #전체 단위를 비교하기 위한 배열과 결과값 변수 설정
    length = []
    result = ""
    # 만약 주어진 값이 1이면 1반환
    if len(s) == 1:
        return 1
    #단위는 전체에서 절반까지만 반복하면 된다
    for cut in range(1, len(s) // 2 + 1): 
        #특정 반복 단위 값과 개수를 변수에 설정
        count = 1
        tempStr = s[:cut] 
        #주어진 단위로 반복한다
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i+cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""
    
    return min(length)
