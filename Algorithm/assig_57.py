def solution(answers):
    # 수포자들의 패턴 정의
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자가 맞힌 문제 수 초기화
    scores = [0, 0, 0]

    # 정답과 패턴을 비교하여 맞힌 문제 수 계산
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            scores[2] += 1

    # 가장 많은 문제를 맞힌 수포자 찾기
    max_score = max(scores)
    result = []
    for i in range(3):
        if scores[i] == max_score:
            result.append(i + 1)

    return result


# 예시 테스트 케이스
print(solution([1, 2, 3, 4, 5]))  # 예상 결과: [1]
print(solution([1, 3, 2, 4, 2]))  # 예상 결과: [1, 2, 3]
