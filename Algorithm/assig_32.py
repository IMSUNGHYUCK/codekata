def solution(a, b):
    inner_product = sum(a[i] * b[i] for i in range(len(a)))
    return inner_product
