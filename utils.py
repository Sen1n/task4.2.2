def fac(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_power_of_five(num):
    """Check if a number is a power of 5."""
    if num == 1:
        return True
    elif num < 1:
        return False
    else:
        while num % 5 == 0:
            num /= 5
        return num == 1
