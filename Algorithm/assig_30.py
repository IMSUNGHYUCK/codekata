def solution(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        # 짝수 길이인 경우 가운데 두 글자 반환
        return s[mid-1:mid+1]
    else:
        # 홀수 길이인 경우 가운데 한 글자 반환
        return s[mid]

word = solution('qwers')

print(word)
