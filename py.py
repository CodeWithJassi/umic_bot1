def mul(*arg):
    product = 1
    for num in arg:
        product *= num
    return product

print(mul(1, 2, 3, 4))