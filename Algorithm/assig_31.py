def solution(n):
    # '수박'을 n//2번 반복하고, n이 홀수일 경우 '수'를 추가로 붙입니다.
    pattern = "수박" * (n // 2) + "수" * (n % 2)
    return pattern

print(solution(6))