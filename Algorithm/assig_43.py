def solution(t, p):
    p_len = len(p)
    p_int = int(p)
    count = 0

    # t에서 p와 같은 길이의 부분 문자열을 순회하며 비교
    for i in range(len(t) - p_len + 1):
        substring = t[i:i + p_len]
        if int(substring) <= p_int:
            count += 1

    return count