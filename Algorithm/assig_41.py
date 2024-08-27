def solution(s):
    # 공백을 기준으로 문자열을 단어로 나눔
    words = s.split(' ')

    # 변환된 단어들을 저장할 리스트
    transformed_words = []

    # 각 단어에 대해 처리
    for word in words:
        transformed_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                transformed_word += word[i].upper()  # 짝수 인덱스 대문자
            else:
                transformed_word += word[i].lower()  # 홀수 인덱스 소문자
        transformed_words.append(transformed_word)

    # 변환된 단어들을 공백으로 결합하여 반환
    return ' '.join(transformed_words)