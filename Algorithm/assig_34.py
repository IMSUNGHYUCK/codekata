def solution(s):
    # 문자열을 정렬된 리스트로 변환 (내림차순 정렬)
    sorted_list = sorted(s, reverse=True)
    # 리스트를 다시 문자열로 변환하여 반환
    return ''.join(sorted_list)