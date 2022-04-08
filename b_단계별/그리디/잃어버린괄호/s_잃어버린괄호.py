



"""
사용한 논리:
처음 - 이전의 값만 양수로 넣고 나머지 - 뒤에 부분은 음수로 계산한다
"""


arr = input().split('-') 
s = 0 
for i in arr[0].split('+'): 
    s += int(i) 
for i in arr[1:]: 
    for j in i.split('+'): 
        s -= int(j) 
print(s)
