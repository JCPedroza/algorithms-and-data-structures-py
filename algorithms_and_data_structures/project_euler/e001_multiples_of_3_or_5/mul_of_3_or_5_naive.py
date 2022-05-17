def mul_of3or5(limit: int) -> int:
    return sum(filter(
        lambda x: x % 3 == 0 or x % 5 == 0,
        range(3, limit)))


solution = mul_of3or5
name = 'naive'
