def solution(n):
    num = str(n)
    number = []
    for i in num:
        number.append(int(i))
    number.sort(reverse=True)

    answer = 0

    for f in number:
        answer = answer * 10 + f

    return answer