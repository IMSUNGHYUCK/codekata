from functools import partial

def sort_key(x, n):
    return (x[n], x)

def solution(strings, n):
    sort_key_with_n = partial(sort_key, n=n)
    return sorted(strings, key=sort_key_with_n)
