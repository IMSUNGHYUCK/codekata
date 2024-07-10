num = [] #리스트 생성
for i in range(1,16): #레인지 함수로 숫자생성
    if i % 2 == 0: #2 로 나눈 나머지가 0이면
        num.append(i*10) #곱하기 10을 해서 넣고
    else:
        num.append(i)# 아니면 그냥 넣어라

print(num)