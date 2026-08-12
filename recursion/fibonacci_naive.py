def fibonacci(n):
    """naive 재귀 피보나치. 같은 값을 반복 계산해서 O(2^n)까지 느려질 수 있다.
    -> 이 중복 계산 문제는 Dynamic Programming에서 해결한다."""
    if n <= 1:                              # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(10))  # 55
    # fibonacci(5)를 구하는 과정에서 fibonacci(3), fibonacci(2) 등이 여러 번 중복 계산된다.
