def solution(numbers):
    # 중복을 허용하지 않으므로 집합을 사용
    result_set = set()

    # numbers 배열에서 서로 다른 인덱스의 두 수를 더하여 집합에 추가
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result_set.add(numbers[i] + numbers[j])

    # 집합을 리스트로 변환하고 오름차순으로 정렬
    result_list = list(result_set)
    result_list.sort()

    return result_list

numbers1 = [2, 1, 3, 4, 1]
print(solution(numbers1))  # 예상 결과: [2, 3, 4, 5, 6, 7]

# 테스트 케이스 2
numbers2 = [5, 0, 2, 7]
print(solution(numbers2))  # 예상 결과: [2, 5, 7, 9, 12]
