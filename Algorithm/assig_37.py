def solution(arr1, arr2):
    # 결과 행렬 초기화
    answer = []

    # 행렬의 행 수와 열 수 추출
    rows = len(arr1)
    cols = len(arr1[0])

    # 행렬 덧셈 수행
    for i in range(rows):
        row = []
        for j in range(cols):
            # 각 위치의 요소를 더해서 새로운 행렬에 추가
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)

    return answer

print(solution([[1,3],[1,4]],[[5,3],[3,4]]))