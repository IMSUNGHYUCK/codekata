from itertools import combinations

def solution(number):
    count = 0
    # 모든 가능한 세 수의 조합을 탐색
    for comb in combinations(number, 3):
        if sum(comb) == 0:
            count += 1
    return count