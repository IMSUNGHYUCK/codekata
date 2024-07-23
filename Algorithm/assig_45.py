def solution(s, n):
    result = []
    for char in s:
        if char.isalpha():
            if char.islower():
                shifted = (ord(char) - ord('a') + n) % 26 + ord('a')
            elif char.isupper():
                shifted = (ord(char) - ord('A') + n) % 26 + ord('A')
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)


# 테스트
print(solution("AB", 1))  # "BC"
print(solution("z", 1))   # "a"
print(solution("a B z", 4))  # "e F d"