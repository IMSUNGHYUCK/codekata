def solution(k, m, score):
    # 점수 배열을 내림차순으로 정렬
    score.sort(reverse=True)

    max_profit = 0
    # m개씩 묶어 상자를 만듦
    for i in range(0, len(score) - m + 1, m):
        # 현재 상자의 최저 점수를 구함
        box = score[i:i + m]
        min_score_in_box = min(box)
        # 상자의 가격을 계산하여 이익에 더함
        max_profit += min_score_in_box * m

    return max_profit