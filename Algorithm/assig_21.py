def solution(x): #값 x을 불러올 solution 함수 생성
    y = [] # 리스트 생성
    for i in str(x): #i 안에다 x를 문자형으로 바꿔서 인덱스값 만큼 반복
        y.append(int(i)) #리스트 y에다 숫자형으로 바꾼 i 저장

    p = x / sum(y) # p변수에다 x에 리스트 y값을 합하여 저장

    if p == int(p): #p와 정수형 p가 같으면
        answer = True # True 반환
    else:
        answer = False # 아니면 False 반환

    return answer

print(solution(50))
