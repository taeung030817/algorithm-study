def two_sum_sorted(arr, target):
    """정렬된 배열에서 합이 target인 두 값의 인덱스를 찾는다. 없으면 None. O(n)."""
    left, right = 0, len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return (left, right)
        elif total < target:
            left += 1
        else:
            right -= 1

    return None


if __name__ == "__main__":
    nums = [1, 2, 4, 6, 8, 9, 14, 15]
    target = 13
    print(two_sum_sorted(nums, target))
