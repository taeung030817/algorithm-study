def fib_memo(n, cache=None):
    """top-down memoization. 계산한 값은 cache에 저장해서 재사용. O(n)."""
    if cache is None:
        cache = {}
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


if __name__ == "__main__":
    print(fib_memo(50))  # naive 재귀로는 사실상 계산 불가능한 크기도 즉시 계산됨
