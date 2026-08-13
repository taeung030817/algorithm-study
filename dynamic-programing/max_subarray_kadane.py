def max_subarray(nums):
    """카데인 알고리즘. 연속 부분 배열의 최대 합. O(n) 시간, O(1) 메모리."""
    current = best = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)   # 이어갈지, 새로 시작할지
        best = max(best, current)

    return best


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray(nums))  # 6  ([4, -1, 2, 1])
