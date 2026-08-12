def is_palindrome(s):
    """양 끝에서 시작하는 두 포인터로 회문 여부를 판별한다. O(n)."""
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))    # False
