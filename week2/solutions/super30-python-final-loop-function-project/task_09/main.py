def is_prime(number):
    """Return whether a number is prime."""
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def prime_analysis(start, end):
    """Return primes and their summary for an inclusive range."""
    if start > end:
        start, end = end, start
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    total = 0
    for number in primes:
        total += number
    return {"primes": primes, "count": len(primes), "total": total, "largest": primes[-1] if primes else None}


print(prime_analysis(1, 10))
