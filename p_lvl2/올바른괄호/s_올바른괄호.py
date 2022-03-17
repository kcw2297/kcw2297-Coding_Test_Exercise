





"""
사용한 논리:
stack을 이용한 풀이이다
원소가 (인 경우에만 append를 하여서 한번만 pop하면된다
"""



def solution(s):
    answer = True
    Queue = []
    for i in s: 
        if i == '(': Queue.append('(')
        else: 
            try: Queue.pop() 
            except: return False
    if len(Queue) == 0: return True
    else: return False

