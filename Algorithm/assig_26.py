def solution(absolutes, signs):
    answer = []
    for i in range(len(signs)):
        if signs[i]:
            answer.append(absolutes[i])
        else:
            answer.append(-absolutes[i])
    return sum(answer)

print(solution([4, 7, 12], [True, False, True]))