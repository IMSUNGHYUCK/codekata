def solution(a, b):
    if a > b:
        a, b = b, a

    sum_of_range = 0
    for num in range(a, b + 1):
        sum_of_range += num

    return sum_of_range

a = list(range(1,30+1))
sum = 0
for b in a:
    sum += b
    print(sum)

