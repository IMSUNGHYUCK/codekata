import heapq


def solution(k, score):
    hall_of_fame = []  # 명예의 전당 (최소 힙)
    result = []

    for day, s in enumerate(score):
        if len(hall_of_fame) < k:
            # 초기 k일까지는 그냥 힙에 추가
            heapq.heappush(hall_of_fame, s)
        else:
            # k일 이후부터는 힙의 최솟값과 비교해서 더 크면 교체
            if s > hall_of_fame[0]:
                heapq.heappushpop(hall_of_fame, s)

        # 현재 힙의 최솟값을 결과에 추가
        result.append(hall_of_fame[0])

    return result

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))  # [10, 10, 10, 20, 20, 100, 100]
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))  # [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]