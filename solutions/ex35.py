# 35
#
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

from util import prime_sieve

primes = prime_sieve(1_000_000)


def is_circular_prime(n):
    n_str = str(n)
    for i, _ in enumerate(n_str):
        rot = n_str[i : len(n_str)] + n_str[0:i]
        if int(rot) not in primes:
            return False
    else:
        return True


def main():
    circular_primes = filter(is_circular_prime, primes)
    return len(list(circular_primes))


if __name__ == "__main__":
    main()
