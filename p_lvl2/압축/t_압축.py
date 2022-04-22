"""https://programmers.co.kr/learn/courses/30/lessons/17684"""


"""
생각한 논리 및 오류:
아스키코드를 활용해 A~Z까지 숫자를 반환하여 초기화한다
입력한 값이 사전에 포함시 다음 문자 확인하고 만약 없으면 확인한대까지 사전 추가

현재 확인한 것의 다음 글자까지 사전에 있는지 확인하고 반환하는 것은 현재 확인값만 추가

처음 접근을 for문을 이용해 idx하나씩 비교하려하였지만 연속적인 값 비교에 어려움에 while문으로 시도
	
"""

def solution(msg):
    answer = []
    dic = {}

    for i in range(0,25):
        dic[chr(65+i)] = i+1


    start, end = 0, 0

    while True:
        
        end += 1

        if end == len(msg):
            answer.append(dic[msg[start:end]]) 
            break

        if msg[start:end+1] not in dic:
            dic[msg[start:end+1]] = len(dic)+1
            answer.append(dic[msg[start:end]])
            start = end

    return answer


# def solution(msg):
#     answer = []
#     dictionary = {}

#     for let in msg:
#         l_num = ord(let) - 65
#         dictionary[let] = l_num
    
#     while msg:
#         for i in range(len(msg)):
#             if msg[i] in dictionary:
                
            


# def solution(msg):
#     answer = []
#     dictionary = {}
#     for idx in range(msg):
#         let_num = ord(msg[idx]) - 64

#         if not dictionary[msg[idx]]:
#             dictionary[msg[idx]] = let_num
#             answer.append(let_num)
#         elif :
            

def solution(msg):
    answer = []
    dic = {}

    for i in range(26):
        dic[chr(65+i)] = i+1

    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer

