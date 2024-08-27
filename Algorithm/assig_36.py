def solution(s):
    # 문자열의 길이가 4 또는 6인지 확인
    if len(s) == 4 or len(s) == 6:
        # 모든 문자가 숫자인지 확인
        if s.isdigit():
            return True
    return False
