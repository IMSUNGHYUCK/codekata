def solution(seoul):
    for i,v in enumerate(seoul):
        if v == "Kim":
            answer = print(f'"김서방은 {i}에 있다"')
    return answer

print(solution(["Jane", "Kim"]))
