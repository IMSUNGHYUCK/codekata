def solution(n):
    b = []
    for i in str(n):
        b.append(i)
    answer = []
    for f in b:
        answer.append(int(f))
    answer = sum(answer)
    return answer


