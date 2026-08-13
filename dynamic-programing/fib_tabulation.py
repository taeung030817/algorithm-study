def fib_tabulation(n):
    """bottom-up tabulation. 앞의 두 값만 있으면 되므로 변수 2개, O(1) 메모리."""
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    print(fib_tabulation(50))
