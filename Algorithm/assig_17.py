def solution(n):
    answer = []
    reversed_str = str(n)[::-1]

    for char in reversed_str:
        answer.append(int(char))
    return answer