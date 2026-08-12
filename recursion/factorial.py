def factorial(n):
    """가장 기본적인 재귀. base case -> 축소 -> 진행."""
    if n <= 1:                     # base case
        return 1
    return n * factorial(n - 1)    # smaller sub-problem, base case로 진행


if __name__ == "__main__":
    print(factorial(5))  # 120
