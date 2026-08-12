def remove_duplicates(arr):
    """정렬된 배열에서 중복을 제자리에서 제거한다 (reader/writer 포인터). 남은 길이를 반환."""
    if not arr:
        return 0

    write = 0
    for read in range(1, len(arr)):
        if arr[read] != arr[write]:
            write += 1
            arr[write] = arr[read]

    return write + 1


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    length = remove_duplicates(nums)
    print(nums[:length])
