
def raise_power(base, exp):
    result = 1
    for index in range(exp):
        result *= base

    return result

print(raise_power(2,3))