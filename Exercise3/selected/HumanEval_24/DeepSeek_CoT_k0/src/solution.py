def largest_divisor(n: int) -> int:
    """Return the largest divisor of n that is less than n."""
    if n <= 1:
        raise ValueError("n must be > 1")

    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
