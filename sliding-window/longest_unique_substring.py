def longest_unique_substring(s):
    """중복 문자가 없는 가장 긴 연속 부분 문자열의 길이를 구한다. 가변 크기 윈도우. O(n)."""
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    print(longest_unique_substring("abcabcbb"))  # 3 ("abc")
