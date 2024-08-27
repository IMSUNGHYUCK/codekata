def solution(numbers):
    # 0부터 9까지의 숫자를 포함한 집합
    full_set = set(range(10))
    # numbers 배열을 집합으로 변환
    numbers_set = set(numbers)
    # full_set에서 numbers_set을 뺀 차집합을 구함
    missing_numbers = full_set- numbers_set
    # 차집합에 있는 숫자들의 합을 반환
    return sum(missing_numbers)

print(solution([1,2,3,4,6,7,8,0,]))