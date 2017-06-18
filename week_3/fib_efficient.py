def fib_efficient(n, d):
    # base cases
    if n == 1:
        d[n] = 1
        return d[n]
    if n == 2:
        d[n] = 2
        return d[n]
    # if already in dictionary, no need to re-compute, return it
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        # save to dictionary
        d[n] = ans
        return ans

print(fib_efficient(5, {}))
