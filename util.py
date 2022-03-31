from functools import reduce
from itertools import count


def triangle_numbers():
    i = 1
    step = 2
    while True:
        yield i
        i += step
        step += 1


def fibonacci():
    n = 1
    n1 = 2
    while True:
        yield n
        n, n1 = n1, n + n1


def fibonacci_until(n):
    fib = fibonacci()
    i = next(fib)
    while i < n:
        yield i
        i = next(fib)


def collatz_sequence(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield n


def multiples(n, until):
    return [i for i in range(n, until, n)]


def primes():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1


def prime_sieve(n):
    sieve = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in sieve:
            sieve -= set(range(i + i, n + 1, i))
    return sieve


def infinite_prime_sieve():
    yield from (2, 3, 5, 7)
    sieve = {}
    ps = infinite_prime_sieve()
    next(ps)
    p = next(ps)
    assert p == 3
    q = p**2
    for i in count(9, 2):
        if i in sieve:
            step = sieve.pop(i)
        elif i < q:
            yield i
            continue
        else:
            assert i == q
            step = 2 * p
            p = next(ps)
            q = p**2
        i += step
        while i in sieve:
            i += step
        sieve[i] = step


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5 + 1), 2):
        if num % i == 0:
            return False
    return True


def prime_factors(num):
    primes = []
    current = 2
    while num != 1:
        if is_prime(current) and num % current == 0:
            num /= current
            primes.append(current)
            continue

        current += 1

    return primes


def divisors(n):
    return sorted(
        set(
            reduce(
                list.__add__,
                [[i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0],
            )
        )
    )


def proper_divisors(n):
    div = divisors(n)
    div.remove(n)
    return div


def sum_digits(n):
    return sum(digits(n))


def digits(n):
    return [int(i) for i in list(str(n))]


def is_palindrome(n):
    lst = list(str(n))
    return lst == list(reversed(lst))
