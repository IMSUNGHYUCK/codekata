def solution(price, money, count):
    # 총 필요한 비용 계산
    total_cost = price * count * (count + 1) // 2

    # 부족한 금액 계산
    shortfall = total_cost - money

    # 부족한 금액이 없으면 0을 반환, 있으면 양수를 반환
    return max(0, shortfall)