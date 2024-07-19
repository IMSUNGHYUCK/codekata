def solution(x):
    y = []
    for i in str(x):
        y.append(int(i))

    p = x / sum(y)

    if p == int(p):
        answer = '하샤드 수 입니다.'
    else:
        answer = '하샤드 수가 아닙니다.'

    return answer

print(solution(50))
