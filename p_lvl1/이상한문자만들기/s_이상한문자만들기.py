



"""
split()함수로 문자열 내에 공간을 분리한 후에 map lamba함수로 안에 조건을
부여하여 최종적으로 join()하는 코드이다. 이로인해 공간 효율성을 적게 먹는
장점이 있다
"""




def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
