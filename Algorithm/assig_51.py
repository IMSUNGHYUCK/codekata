def solution(food):
    left_side = ""

    for i in range(1, len(food)):
        # 음식의 개수 절반을 문자열로 변환하여 추가
        left_side += str(i) * (food[i] // 2)

    # 중앙에 물('0')을 추가하고, left_side의 역순을 붙임
    result = left_side + '0' + left_side[::-1]

    return result

# 테스트 케이스 1
food1 = [1, 3, 4, 6]
print(solution(food1))  # 예상 결과: "1223330333221"

# 테스트 케이스 2
food2 = [1, 7, 1, 2]
print(solution(food2))  # 예상 결과: "111303111"
