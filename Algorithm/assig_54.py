def solution(a, b):
    # 각 월의 일수
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 요일 배열
    days_of_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    # 해당 월까지의 일수를 더함
    days = sum(days_in_month[:a - 1]) + b - 1

    # 요일 계산
    day_of_week = days_of_week[days % 7]

    return day_of_week


# 예제 테스트
print(solution(5, 24))  # "TUE"
print(solution(1, 1))  # "FRI"
print(solution(12, 31))  # "SAT"
