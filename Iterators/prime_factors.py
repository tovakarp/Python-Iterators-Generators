def get_prime_factors_generator(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            yield i
    if num > 1:
        yield num


for x in get_prime_factors_generator(100):
    print(x)