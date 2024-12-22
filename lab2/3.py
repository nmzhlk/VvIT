def is_prime(number):
    dels = set()
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            dels.add(n)
            dels.add(number * n)
    return len(dels) == 0


print(is_prime(int(input())))
