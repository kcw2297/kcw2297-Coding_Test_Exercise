"""https://programmers.co.kr/learn/courses/30/lessons/17683"""


"""
사용한 논리 및 오류 :
1.주어진 m을 배열에 저장하는데, #은 소문자로 치환한다
2. 멜로디의 순서도 배열로 저장하는데, #은 소문자로 치환한다
3. 시간의 경우 시간*60을 하여서 분으로 치환한다
4. 각 음을 부분비교를한다
*조건이 일치하는게 여러개인 경우 재생 시간이 긴 것을 반환, 재생 시간도 같으면 먼저 입력된 제목 반환
*조건이 일치하는게 없다면 None 반환

*위에 정리한 논리대로 구현을 하였지만 시간초과로 인한 효율성에 막혔다
-while문과 for문을 중첩하여서 O(n^2)를 만들었다 (replace가 1개의 문자만 변형하는 줄 안 실수이다)
-for문 안에 while문을 또 사용하여 O(n^2)를 만들었다 (마찬가지로 replace가 1개의 문자만 변형하는 줄 안 실수이다)
"""

def check(m, rhythm):
    if m in rhythm:
        return True
    else:
        return False


def solution(m, musicinfos):

    # '#'이 있는 동안에는 for문을 이용해 해당 인덱스의 음을 소문자로 변환한다
    while '#' in m:
        for idx in range(len(m)):
            if m[idx] == '#':
                m.replace(m[idx-1:idx+1], m[idx].lower())
            break
    
    infos = []
    
    for info in musicinfos:
        # find out repeating numbers
        separate = info.split(',')
        h1 = int(separate[0][:2])*60
        m1 = int(separate[0][3:])
        time1 = h1 + m1
        h2 = int(separate[1][:2])*60
        m2 = int(separate[1][3:])
        time2 = h2 + m2
        repeat = time2 - time1

        total_word = separate[-1]*(repeat // len(separate[-1])) + separate[-1][:(repeat % len(separate[-1]))]

        while '#' in total_word:
            for idx in range(len(total_word)):
                if total_word[idx] == '#':
                    total_word.replace(total_word[idx-1:idx+1], total_word[idx].lower())
                break
        
        # append(time, name, rhythm)
        infos.append([repeat ,separate[2], total_word])


    test = []
    for info in infos:
        if check(m, info[-1]):
            test.append(info)

    if test == []:
        return '(None)' 

    curr = test[0]
    for com in test:
        if curr[0] < com[0]:
            curr = com
    
    return curr[1]