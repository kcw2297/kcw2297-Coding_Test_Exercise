




[0,1,1,1]
[1,1,0,1]
[1,1,1,1]
[0,0,1,0] => 4

def solution(board):
    n = len(board)
    m = len(board[0])

    # dp 준비
    #전체 테이블을 0으로 만든다
    dp = [[0]*m for _ in range(n)]
    #첫 행을 가져온다
    dp[0] = board[0]
    #첫 열을 가져온다
    for i in range(1,n):
        dp[i][0] = board[i][0]
    
    # 2중 포문으로 연산
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    # 최대 넓이 구하기
    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)
    
    return answer**2
