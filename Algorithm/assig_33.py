def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                count += 1
            else:
                count += 2
    return count

def solution(left, right):
    result = 0
    for num in range(left, right + 1):
        if count_divisors(num) % 2 == 0:
            result += num
        else:
            result -= num
    return result

a = solution(13,17)
print(a)
