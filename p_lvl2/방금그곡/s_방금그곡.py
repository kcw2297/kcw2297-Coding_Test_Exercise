

"""
모든 조건문들을 마지막에 or로 표시함으로써 코드의 오류를 줄이고 가독성을 높혔다
or과 and의 적용 순서를 적절히 배치하여 모든 조건을 만족한다

항상 split한 값을 새로운 리스트에 저장하여 메모리 효율성을 떨여트렸는데,
이를 고려한 공간 효율성까지 높이는 습관을 들이자
"""

import math

def solution(m, musicinfos):
    answer = None
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(",")
        
        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute
        
        hour, minute = map(int, end.split(":"))
        end = hour * 60 + minute
        duration = end - start
        
        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        code *= math.ceil(duration / len(code))
        code = code[:duration]
        
        if m not in code:
            continue
            
        if answer == None or answer[0] < duration or (answer[0] == duration and answer[1] > start):
                answer = (duration, start, title)
    
    if answer:
        return answer[-1]
    
    return "(None)"



"""
사용한 논리:
사용한 논리는 동일하지만 공간 메모리 사용에서 훨씬 효율적으로 작성된  코드이다
"""


def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0,'(None)']   # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length>answer[0]:
            answer=[time_length,title]
    return answer[-1]

