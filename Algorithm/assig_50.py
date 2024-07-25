def solution(s):
    result = []
    last_seen = {}

    for i, char in enumerate(s):
        if char in last_seen:
            result.append(i - last_seen[char])
        else:
            result.append(-1)

        last_seen[char] = i

    return result
s1 = "banana"
print(solution(s1))  # 예상 결과: [-1, -1, -1, 2, 2, 2]

# 테스트 케이스 2
s2 = "foobar"
print(solution(s2))  # 예상 결과: [-1, -1, 1, -1, -1, -1]