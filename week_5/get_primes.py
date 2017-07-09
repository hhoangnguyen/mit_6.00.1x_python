def genPrimes():
    """
    Have the generator keep a list of the primes it's generated.
    A candidate number x is prime if (x % p) != 0 for all earlier primes p.
    """
    yield 2
    primes_list = [2]

    # start from 3
    candidate = 3
    while True:
        is_prime = True
        for prime in primes_list:
            # not a prime
            if (candidate % prime) == 0:
                is_prime = False
                # move on to next candidate
                candidate += 1
                # no need to iterate the rest of the list
                break

        # candidate is a prime number
        if is_prime:
            primes_list.append(candidate)
            print(candidate)
            yield candidate

primes = genPrimes()
primes.__next__()
primes.__next__()
primes.__next__()
primes.__next__()
primes.__next__()
primes.__next__()
primes.__next__()
