def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        # 배열의 i번째부터 j번째까지 자른 후 정렬
        sliced_array = sorted(array[i-1:j])
        # 정렬된 배열의 k번째 값을 결과 리스트에 추가
        result.append(sliced_array[k-1])
    return result

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))  # [5, 6, 3]