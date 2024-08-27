def solution(arr):
    # 배열이 비어있는 경우를 처리합니다.
    if not arr:
        return [-1]

    # 배열에서 가장 작은 값을 찾습니다.
    min_value = min(arr)

    # 가장 작은 값을 제거한 새로운 배열을 만듭니다.
    arr.remove(min_value)

    # 배열이 빈 배열이 된 경우 [-1]을 반환합니다.
    if not arr:
        return [-1]

    # 그렇지 않은 경우 배열을 반환합니다.
    return arr