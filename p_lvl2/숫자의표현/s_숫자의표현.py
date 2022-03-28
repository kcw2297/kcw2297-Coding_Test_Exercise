



"""
사용한 논리:
https://gkalstn000.github.io/2021/01/21/%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84/


등차수열의 합공식에서 a가 자연수가 되기 위해 k가 자연수가 되어야만하기에 
k는 n의 약수 중에 홀수이어야만한다
*예외로 k가 2인 경우에는 특수하게 가능하다
"""







def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])