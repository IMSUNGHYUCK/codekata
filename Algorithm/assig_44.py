def solution(sizes):
    # 명함의 가로와 세로 중 큰 값을 항상 가로로 보고, 작은 값을 세로로 봄
    max_width = 0
    max_height = 0

    for size in sizes:
        width, height = size
        if width < height:
            width, height = height, width
        max_width = max(max_width, width)
        max_height = max(max_height, height)

    return max_width * max_height