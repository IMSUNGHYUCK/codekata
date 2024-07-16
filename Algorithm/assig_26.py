def solution(phone_number):
    # 뒷 4자리를 제외한 나머지를 *로 변환
    masked_part = '*' * (len(phone_number) - 4)
    # 뒷 4자리
    visible_part = phone_number[-4:]
    # 결합하여 반환
    return masked_part + visible_part

# 테스트 예시
print(solution("01033334444"))  # "*******4444"
print(solution("027778888"))    # " *****8888"


