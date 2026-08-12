def max_sum_fixed_window(arr, k):
    """크기 k인 고정 윈도우 중 합이 최대인 값을 구한다. 슬라이딩하며 빼고 더하기만 함. O(n)."""
    if len(arr) < k:
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]   # 들어오는 값 더하고, 나가는 값 빼기
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    nums = [4, 2, 7, 1, 5, 3]
    print(max_sum_fixed_window(nums, 3))  # 13
